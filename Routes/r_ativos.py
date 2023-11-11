from flask import Blueprint, request
from Controllers.auth.auth import Auth
from Controllers.ativos import get_ativos, createAtivos, excluirAtivos, updateAtivos, selectById
from flask_restx import Resource, Namespace, fields

ativos = Namespace('ativos', description="Rota para manipulação de ativos")

ativosPOSTModel = ativos.model("Cadastro de ativos", {
    "dataCadastroProduto": fields.Date(required=True, description="Data de cadastro do produto", example="2005-05-21"),
    "nomeProduto": fields.String(required=True, description="Nome do produto", example="Fonte 350w"),
    "qntProduto": fields.Integer(required=True, description="Quantidade do produto", example="25"),
    "valorPagoProduto": fields.Float(required=True, description="Valor pago pelo produto", example="250.34"),
    "tipoProduto": fields.String(required=True,
                                 description="Classificação do produto. Valores: (P)eriféricos | (D)ecorações | (M)óveis | (E)letrônicos",
                                 example="P"),
    "descricaoProduto": fields.String(required=True, description="Descrição do produto",
                                      example="Fonte com selo 80plus"),
})
ativosModel = ativos.inherit("Ativos com os campos", ativosPOSTModel, {
        "id": fields.Integer(required=True, description="Id único do ativo", example=1)})

serverError = ativos.model("ServerError", {
    "error": fields.String(description="Erro referido")
})


@Auth
@ativos.route("/")
class Ativos(Resource):
    @ativos.expect(ativosPOSTModel)
    @ativos.doc(description='''Rota utilizada para cadastro de ativos,
                               nela é necessário informar os dados referentes ao ativo a ser cadastro''')
    @ativos.response(201, "Criado com sucesso!")
    @ativos.response(500, "Erro no servidor", serverError)
    def post(self):
        return createAtivos(request.data)

    @ativos.doc(description='''Rota utilizada para busca de ativos,
                               ela retorna todos os ativos referentes a determinado cadastro''')
    @ativos.response(200, "Buscado com sucesso!", [ativosModel])
    @ativos.response(500, "Erro no servidor", serverError)
    def get(self):
        return get_ativos()

    @ativos.expect(ativosModel)
    @ativos.response(200, "Alterado com sucesso!")
    @ativos.response(204, "Sem conteúdo")
    @ativos.response(500, "Erro no servidor", serverError)
    @ativos.doc(description='''Rota utilizada para edição de ativos,
                                 nela é necessário informar os dados referentes ao ativo a ser editado''')
    def put(self):
        return updateAtivos(request.data)


@ativos.route("/<id>")
class AtivosId(Resource):
    @ativos.doc(description='''Rota utilizada para busca de um único ativo tendo como base seu ID,
                               é necessário inserir o ID referente ao ativo a ser buscado''')
    @ativos.response(200, "Buscado com sucesso!", ativosModel)
    @ativos.response(204, "Sem conteúdo")
    @ativos.response(500, "Erro no servidor", serverError)
    def get(self, id):
        return selectById(id)

    @ativos.doc(description='''Rota utilizada para remoção de ativos,
                                   é necessário inserir o id referente ao ativo a ser removido''')

    @ativos.response(200, "deletado com sucesso!")
    @ativos.response(204, "Sem conteúdo")
    @ativos.response(500, "Erro no servidor", serverError)
    def delete(self, id):
        return excluirAtivos(id)

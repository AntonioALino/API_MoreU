from Controllers.auth.auth import Auth
from Controllers.clientes import get_clientes, createClientes, excluirClientes, updateClientes, login
from flask import request
from flask_restx import Resource, Namespace, fields

clientes = Namespace('clientes', description="Rota para manipulação de clientes")

clientesGETModel = clientes.model("Busca de clientes", {
    "nome": fields.String(required=True, description="Nome do cliente", example="Pedro Augusto"),
    "email": fields.String(required=True, description="Email do cliente", example="cliente@email.com"),
    "contato": fields.Integer(required=True, description="Número de telefone do cliente", example="12345678910"),
    "nomeEmpresa": fields.String(required=True, description="Nome da empresa a qual o cliente é sócio/colaborador", example="Empresa LTDA")
})

clientesPOSTModel = clientes.inherit("Cadastro de clientes", clientesGETModel, {
    "password": fields.String(required=True, description="Senha do cliente", example='9Qv15).=5"^n')
})

clientesModel = clientes.inherit("cliente com todos os campos", clientesPOSTModel, {
        "id": fields.Integer(required=True, description="Id único do cliente", example=1)})

loginModel = clientes.model("Login", {
    "email": fields.String(required=True, description="Email do cliente", example="cliente@email.com"),
    "password": fields.String(required=True, description="Senha do cliente", example='9Qv15).=5"^n')
})

serverError = clientes.model("ServerError", {
    "error": fields.String(description="Erro referido")
})

@clientes.route("/")
class Clientes(Resource):

    @clientes.doc(description='''Rota utilizada para busca de clientes,
                               ela retorna todos os clientes referentes a determinado cadastro''')
    @clientes.response(200, "Buscado com sucesso!", [clientes.inherit("Buscar clientes", clientesGETModel, {
        "id": fields.Integer(required=True, description="Id único do cliente", example=1)})])
    @clientes.response(500, "Erro no servidor", serverError)
    def get(self):
        return get_clientes()

    @clientes.expect(clientesPOSTModel)
    @clientes.doc(description='''Rota utilizada para cadastro de clientes,
                                 nela é necessário informar os dados referentes ao cliente a ser cadastro''')
    @clientes.response(201, "Criado com sucesso!")
    @clientes.response(500, "Erro no servidor", serverError)
    def post(self):
        req = request.data
        return createClientes(req)


    @clientes.doc(description='''Rota utilizada para edição de clientes,
                                 nela é necessário informar os dados referentes ao cliente a ser editado''')
    @clientes.expect(clientesModel)
    @clientes.response(200, "Alterado com sucesso!")
    @clientes.response(204, "Sem conteúdo")
    @clientes.response(409, "Conflito. Email já cadastrado")
    @clientes.response(500, "Erro no servidor", serverError)
    @Auth
    def put(self, user):
        req = request.data
        return updateClientes(req, user)


    @clientes.doc(description='''Rota utilizada para remoção de clientes''')

    @clientes.response(200, "deletado com sucesso!")
    @clientes.response(204, "Sem conteúdo")
    @clientes.response(500, "Erro no servidor", serverError)
    @Auth
    def delete(self, user):
        return excluirClientes(user)

@clientes.route("/login")
class ClientesLogin(Resource):

    @clientes.expect(loginModel)
    @clientes.doc(description='''Rota utilizada para login de clientes,
                                     nela é necessário informar os dados referentes ao cliente a ser autenticado''')
    @clientes.response(201, "Autenticado com sucesso!")
    @clientes.response(500, "Erro no servidor", serverError)
    def post(self):
        req = request.data
        return login(req)

# Importando bibliotecas necessárias
from Controllers.auth.auth import Auth
from Controllers.clientes import get_clientes, createClientes, excluirClientes, updateClientes, login, getClienteById
from flask import request
from flask_restx import Resource, Namespace, fields

# Criando um Namespace para clientes
clientes = Namespace('clientes', description="Rota para manipulação de clientes")

# Definindo o modelo para busca de clientes (GET)
clientesGETModel = clientes.model("Busca de clientes", {
    "nome": fields.String(required=True, description="Nome do cliente", example="Pedro Augusto"),
    "email": fields.String(required=True, description="Email do cliente", example="cliente@email.com"),
    "contato": fields.Integer(required=True, description="Número de telefone do cliente", example="12345678910"),
    "nomeEmpresa": fields.String(required=True, description="Nome da empresa a qual o cliente é sócio/colaborador", example="Empresa LTDA")
})

# Definindo o modelo para cadastrar clientes (POST)
clientesPOSTModel = clientes.inherit("Cadastro de clientes", clientesGETModel, {
    "password": fields.String(required=True, description="Senha do cliente", example='9Qv15).=5"^n')
})

# Definindo o modelo para clientes com todos os campos (GET, PUT, DELETE)
clientesModel = clientes.inherit("cliente com todos os campos", clientesPOSTModel, {
        "id": fields.Integer(required=True, description="Id único do cliente", example=1)})

# Definindo o modelo para login
loginModel = clientes.model("Login", {
    "email": fields.String(required=True, description="Email do cliente", example="cliente@email.com"),
    "password": fields.String(required=True, description="Senha do cliente", example='9Qv15).=5"^n')
})

# Definindo o modelo para erros de servidor
serverError = clientes.model("ServerError", {
    "error": fields.String(description="Erro referido")
})

# Criando a classe de recurso para a rota '/'
@clientes.route("/")
class Clientes(Resource):
    # Rota para buscar clientes
    @clientes.doc(description='''Rota utilizada para busca de clientes,
                               ela retorna todos os clientes referentes a determinado cadastro''')
    @clientes.response(200, "Buscado com sucesso!", [clientes.inherit("Buscar clientes", clientesGETModel, {
        "id": fields.Integer(required=True, description="Id único do cliente", example=1)})])
    @clientes.response(500, "Erro no servidor", serverError)
    def get(self):
        return get_clientes()

    # Rota para cadastrar clientes
    @clientes.expect(clientesPOSTModel)
    @clientes.doc(description='''Rota utilizada para cadastro de clientes,
                                 nela é necessário informar os dados referentes ao cliente a ser cadastro''')
    @clientes.response(201, "Criado com sucesso!")
    @clientes.response(409, "Conflito. Email já cadastrado")
    @clientes.response(500, "Erro no servidor", serverError)
    def post(self):
        req = request.data
        return createClientes(req)


    # Rota para editar clientes
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

    # Rota para excluir clientes
    @clientes.doc(description='''Rota utilizada para remoção de clientes''')

    @clientes.response(200, "deletado com sucesso!")
    @clientes.response(204, "Sem conteúdo")
    @clientes.response(500, "Erro no servidor", serverError)
    @Auth
    def delete(self, user):
        return excluirClientes(user)

# Criando a classe de recurso para a rota '/login'
@clientes.route("/login")
class ClientesLogin(Resource):
    # Rota para realizar login de clientes
    @clientes.expect(loginModel)
    @clientes.doc(description='''Rota utilizada para login de clientes,
                                     nela é necessário informar os dados referentes ao cliente a ser autenticado''')
    @clientes.response(401, "Email/senha incorreto")
    @clientes.response(200, "Autenticado com sucesso!")
    @clientes.response(204, "Sem conteúdo")
    @clientes.response(500, "Erro no servidor", serverError)
    def post(self):
        req = request.data
        return login(req)

# Criando a classe de recurso para a rota '/id'
@clientes.route("/id")
class ClientesId(Resource):
    # Rota para buscar cliente pelo ID
    @clientes.response(200, "Autenticado com sucesso!")
    @clientes.response(204, "Sem conteúdo")
    @clientes.response(500, "Erro no servidor", serverError)
    @Auth
    def get(user, self):
        return getClienteById(user)
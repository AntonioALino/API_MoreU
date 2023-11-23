# Importando as bibliotecas necessárias
from flask import Flask
from flask_cors import CORS
from flask_restx import Api

# Importando os rotas necessários
from Routes.r_ativos import ativos
from Routes.r_clientes import clientes

# Iniciando o aplicativo Flask
app = Flask(__name__)

# Configurando as autorizações para a API
authorizations = {
    "bearerAuth": {
        "type": "apiKey",
        "scheme": "bearer",
        "bearerFormat": "JWT",
        "in": "header",
        "name": "Authorization"
    }
}

# Inicializando a instância da API Flask-RESTx
api = Api(app, version="1.0",
          title="Documentação da API do sistema de ativos MoreU",
          description="API desenvolvida para realização da manipulação de dados do sistema de ativos MoreU, coletando dados enviados do frontend por meio de requisições e caminhos de URL, tratando eles no backend e inserindo/buscando/atualizando na base de dados e, por fim, entregando-os ao frontend novamente.",
          authorizations=authorizations,
          security="http",  
          doc="/doc")
CORS(app, expose_headers="Authorization")

# Desativando a ordenação automática das chaves JSON
app.config['JSON_SORT_KEYS'] = False

# Adicionando os namespaces (blueprints) à API
api.add_namespace(ativos)
api.add_namespace(clientes)

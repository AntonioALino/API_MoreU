from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from Routes.r_ativos import ativos
from Routes.r_clientes import clientes

app = Flask(__name__)

api = Api(app, version="1.0",
          title="Documentação da API do sistema de ativos MoreU",
          description="API desenvolvida para realização da manipulação de dados do sistema de ativos MoreU, coletando dados enviados do frontend por meio de requisições e caminhos de URL, tratando eles no backend e inserindo/buscando/atualizando na base de dados e, por fim, entregando-os ao frontend novamente.", doc="/doc")
CORS(app, expose_headers="Authorization")

app.config['JSON_SORT_KEYS'] = False

api.add_namespace(ativos)

api.add_namespace(clientes)

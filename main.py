from flask import Flask
from flask_cors import CORS
from Routes.r_ativos import ativos
from Routes.r_clientes import clientes

app = Flask(__name__)

CORS(app)

app.config['JSON_SORT_KEYS'] = False

app.register_blueprint(ativos)

app.register_blueprint(clientes)

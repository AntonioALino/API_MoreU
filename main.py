from flask import Flask
from Routes.r_ativos import ativos
from Routes.r_clientes import clientes

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

app.register_blueprint(ativos)

app.register_blueprint(clientes)

app.run(port=5000, host='localhost', debug=True)
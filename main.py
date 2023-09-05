from flask import Flask
from Routes.r_ativos import ativos
from Routes.r_clientes import clientes
from Routes.r_fornecedores import fornecedores


app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

app.register_blueprint(ativos)

app.register_blueprint(clientes)

app.register_blueprint(fornecedores)



app.run(port = 5000, host = 'localhost', debug = True)
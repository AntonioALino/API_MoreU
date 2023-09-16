<<<<<<< HEAD
from flask import Flask
from flask_cors import CORS

=======
from flask import Flask, jsonify
>>>>>>> 238705c34f15f03e0f503af19ab0f94435c2cd68
from Routes.r_ativos import ativos
from Routes.r_clientes import clientes

app = Flask(__name__)

CORS(app)

app.config['JSON_SORT_KEYS'] = False

app.register_blueprint(ativos)

app.register_blueprint(clientes)


app.run(port=5000, host='localhost', debug=True)
from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from bd import dadosAtivos

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moreu.db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)
app.config['JSON_SORT_KEYS'] = False

@app.route('/ativos', methods = ['GET'])
def get_ativos():
  return make_response (
   jsonify(dadosAtivos) 
   )

@app.route('/ativos', methods = ['POST'])
def createAtivos():
  ativo = request.json
  dadosAtivos.append(ativo)
  return make_response(
    jsonify(ativo)
  )

#Consultar por ID
@app.route('/ativos/<int:id>', methods=['GET'])
def obterAtivosPorID(id):
  for ativo in dadosAtivos:
    if ativo.get('id') == id:
      return jsonify(ativo)
#Editar
@app.route('/ativos/<int:id>', methods=['PUT'])
def editarAtivos():
  ativoAlterado = request.get_json()
  for indice, ativo in enumerate (dadosAtivos):
    if ativo.get('id') == id:
      dadosAtivos[indice].update(editarAtivos)
      return jsonify(dadosAtivos[indice])

#Excluir
@app.route('/ativos/<int:id>', methods=['DELETE'])
def excluirAtivos(id):
  for indice, ativo in enumerate(dadosAtivos):
    if ativo.get('id' == id):
      del dadosAtivos[indice]

      return jsonify(dadosAtivos)


app.run()
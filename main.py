
from Controllers.ativos import get_ativos, createAtivos
from flask import Flask, make_response, jsonify, request 
from sqlalchemy.orm import Session
from bd import dadosAtivos
from Models.schema import Ativos
from Models.database import engine

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

@app.route('/ativos', methods = ['GET'])
def execute1():
    get_ativos()

@app.route('/ativos', methods = ['POST'])
def execute2():
  get_json = request.json()
  createAtivos(get_json)
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


app.run(port = 5000, host = 'localhost', debug = True)
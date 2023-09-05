
from Controllers.ativos import get_ativos, createAtivos, excluirAtivos
from flask import Flask, jsonify, request
from bd import dadosAtivos


app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

@app.route('/ativos', methods = ['GET'])
def execute1():
    return get_ativos()

@app.route('/ativos', methods = ['POST'])
def execute2():

  req = request.data

  return createAtivos(req)
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
@app.route('/ativos/<id>',methods=['DELETE'])

def execute3(id):
  return excluirAtivos(id)

app.run(port = 5000, host = 'localhost', debug = True)
import json
from Controllers.clientes import get_clientes, createClientes, excluirClientes, updateClientes
from flask import jsonify, render_template, request, Blueprint
from werkzeug.exceptions import HTTPException

clientes = Blueprint('clientes',__name__)

@clientes.route('/clientes', methods = ['GET'])
def execute1():
    return get_clientes()

@clientes.route('/clientes', methods = ['POST'])
def execute2():

  req = request.data

  return createClientes(req)

#Editar
@clientes.route('/clientes', methods=['PUT'])
def execute4():
  req = request.data
  return updateClientes(req)

#Excluir
@clientes.route('/clientes/<id>',methods=['DELETE'])

def execute3(id):
  return excluirClientes(id)


from Controllers.clientes import get_clientes, createClientes, excluirClientes, updateClientes
from flask import Flask, request, Blueprint

clientes = Blueprint('clientes',__name__)

@clientes.route('/clientes', methods = ['GET'])
def execute1():
    return get_clientes()

@clientes.route('/ativos', methods = ['POST'])
def execute2():

  req = request.data

  return createClientes(req)

#Editar
@clientes.route('/clientes/', methods=['PUT'])
def execute4():
  req = request.data
  return updateClientes(req)

#Excluir
@clientes.route('/ativos/<id>',methods=['DELETE'])

def execute3(id):
  return excluirClientes(id)
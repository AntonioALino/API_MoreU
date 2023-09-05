from Controllers.fornecedores import get_fornecedores, createfornecedores, excluirfornecedores, updatefornecedores
from flask import request, Blueprint

fornecedores = Blueprint('fornecedores', __name__)

@fornecedores.route('/fornecedores', methods = ['GET'])
def execute1():
    return get_fornecedores()

@fornecedores.route('/fornecedores', methods = ['POST'])
def execute2():

  req = request.data

  return createfornecedores(req)

#Editar
@fornecedores.route('/fornecedores', methods=['PUT'])
def execute4():
  req = request.data
  return updatefornecedores(req)

#Excluir
@fornecedores.route('/fornecedores/<id>',methods=['DELETE'])

def execute3(id):
  return excluirfornecedores(id)


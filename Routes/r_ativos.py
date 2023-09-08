from flask import Blueprint, request
from Controllers.ativos import get_ativos, createAtivos, excluirAtivos, updateAtivos

ativos = Blueprint('ativos', __name__)


@ativos.route('/ativos', methods=['GET'])
def execute1():
    return get_ativos()


@ativos.route('/ativos', methods=['POST'])
def execute2():
    req = request.data

    return createAtivos(req)


@ativos.route('/ativos/', methods=['PUT'])
def execute4():
    req = request.data
    return updateAtivos(req)


@ativos.route('/ativos/<id>', methods=['DELETE'])
def execute3(id):
    return excluirAtivos(id)

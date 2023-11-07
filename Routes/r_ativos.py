from flask import Blueprint, request
from Controllers.auth.auth import Auth
from Controllers.ativos import get_ativos, createAtivos, excluirAtivos, updateAtivos, selectById

ativos = Blueprint('ativos', __name__)


@ativos.route('/ativos', methods=['GET'])
@Auth
def execute1():
    return get_ativos()


@ativos.route('/ativos', methods=['POST'])
@Auth()
def execute2():
    req = request.data

    return createAtivos(req)


@ativos.route('/ativos/', methods=['PUT'])
@Auth()
def execute4():
    req = request.data
    return updateAtivos(req)


@ativos.route('/ativos/<id>', methods=['DELETE'])
@Auth()
def execute3(id):
    return excluirAtivos(id)

@ativos.route('/ativos/<id>', methods=['GET'])
@Auth()
def execute5(id):
    return selectById(id)

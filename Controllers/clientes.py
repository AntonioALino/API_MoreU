# Importando bibliotecas necessárias
import os

from bcrypt import gensalt, hashpw, checkpw
from flask import make_response, jsonify, request
from jwt import encode
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, delete, update
from Models.schema import Clientes
from Models.database import engine
from json import loads
from bcrypt import gensalt, hashpw
from sqlalchemy.exc import IntegrityError

# Função para obter todos os clientes
def get_clientes():
    try:
        with Session(engine) as session:
            # Consulta para obter todos os clientes
            clientes = select(Clientes)

            jsonClientes = []

            # Itera sobre os resultados da consulta e cria uma lista de dicionários
            for cliente in session.scalars(clientes):
                jsonClientes.append({
                    "id": int(cliente.id),
                    "nome": str(cliente.nome),
                    "email": str(cliente.email),
                    "contato": str(cliente.contato),
                    "nomeEmpresa": str(cliente.nomeEmpresa)

                })
            # Cria uma resposta HTTP com os clientes em formato JSON
            response = make_response(
                jsonify(jsonClientes), 200

            )
            response.headers["Content-Type"] = "application/json"

            return response

    except OSError:
        # Em caso de erro, retorna uma resposta de erro com status 500
        response = make_response(
            jsonify({"error": OSError}), 500

        )
        response.headers["Content-Type"] = "application/json"

        return response

# Função para criar um novo cliente
def createClientes(form):
    form_get = loads(form)
    with Session(engine) as session:
        # Hash da senha utilizando bcrypt
        password = form_get["password"].encode("utf8")
        salt = gensalt()
        hash = hashpw(password, salt)

        # Cria uma instância da classe Clientes com os dados fornecidos
        cliente = Clientes(nome=form_get["nome"],
                           email=form_get["email"],
                           contato=form_get["contato"],
                           nomeEmpresa=form_get["nomeEmpresa"],
                           password=hash)

        session.add(cliente)
        try:
            # Commit para manter o novo cliente no banco de dados
            session.commit()

            # Gera um token JWT para o novo cliente
            token = encode({"userId": str(cliente.id)}, os.environ.get("JWT_SECRET"))
            response = make_response(jsonify({"token": token}), 201)
            response.headers["Content-Type"] = "application/json"

            return response
        except IntegrityError:
            # Em caso de erro de integridade (email duplicado), retorna uma resposta de conflito com status 409
            session.rollback()
            return make_response("", 409)

        except OSError:
            return make_response({"error": OSError}, 500)

# Função para excluir um cliente com base no ID do cliente
def excluirClientes(idCliente):
    try:
        with Session(engine) as session:
            # Cria uma instrução DELETE para excluir o cliente específico
            delete_itens = delete(Clientes).where(Clientes.id == idCliente)

            exec_del = session.execute(delete_itens)

            session.commit()

            # Verifica se algum cliente foi excluído e retorna a resposta apropriada
            if (exec_del.rowcount == 0):
                return make_response("", 204)

            response = make_response("", 200)
            response.headers["Content-Type"] = "application/json"

            return response

    except OSError:
        # Em caso de erro, retorna uma resposta de erro com status 500
        response = make_response(
            jsonify({"error": OSError}), 500

        )
        response.headers["Content-Type"] = "application/json"

        return response

# Função para atualizar os dados de um cliente com base no formulário e no ID do cliente
def updateClientes(form, user):
    form_get = loads(form)
    try:
        with Session(engine) as session:
            # Cria uma instrução UPDATE para atualizar os dados do cliente específico
            update_itens = (
                update(Clientes)
                .where(Clientes.id == user)
                .values(nome=form_get['nome'],
                        email=form_get['email'],
                        contato=form_get['contato'],
                        nomeEmpresa=form_get['nomeEmpresa']))

        exec_up = session.execute(update_itens)
        session.commit()

        # Verifica se algum cliente foi atualizado e retorna a resposta apropriada
        if (exec_up.rowcount == 0):
            return make_response("", 204)

        response = make_response(
            "", 200
        )
        return response
    

    except IntegrityError:
        # Em caso de erro de integridade (email duplicado), retorna uma resposta de conflito com status 409
        session.rollback()

        return make_response("", 409)


    except OSError:
        # Em caso de erro, retorna uma resposta de erro com status 500
        response = make_response(
            jsonify({"error": OSError}), 500

        )
        response.headers["Content-Type"] = "application/json"

        return response

# Função para autenticar um cliente e gerar um token JWT
def login(data):
    login_data = loads(data)
    try:
        with Session(engine) as session:
            # Consulta para obter o cliente com o email fornecido
            queryRecept = select(Clientes).where(Clientes.email == login_data["email"])

            exec_select = session.execute(queryRecept).first()

            if exec_select:
                # Verifica a senha utilizando bcrypt
                password = login_data["password"].encode("utf-8")
                if checkpw(password, exec_select[0].password.encode("utf-8")):
                    # Gera um token JWT para o cliente autenticado
                    token = encode({"userId": str(exec_select[0].id)}, os.environ.get("JWT_SECRET"))

                    response = make_response(jsonify({"token": token}), 200)

                # Em caso de senha incorreta, retorna uma resposta não autorizada com status 401
                else:
                    response = make_response("", 401)

            else:
                # Em caso de email não encontrado, retorna uma resposta vazia com status 204
                response = make_response("", 204)

        return response

    except OSError:
        # Em caso de erro, retorna uma resposta de erro com status 500
        response = make_response(
            jsonify({"error": OSError}), 500

        )
        response.headers["Content-Type"] = "application/json"

        return response

# Função para obter o nome de um cliente com base no ID do cliente
def getClienteById(id):

    try:
        with Session(engine) as session:
            # Consulta para obter o cliente com o ID fornecido
            query = select(Clientes).where(Clientes.id == id)

            exec = session.execute(query).first()

            # Verifica se o cliente foi encontrado e retorna a resposta apropriada
            if exec:
                response = make_response(jsonify({"nomeUsuario": exec[0].nome}), 200)

            else:
                response = make_response("", 204)

            return response

    except Exception as E:
        # Em caso de erro, retorna uma resposta de erro com status 500
        response = make_response(jsonify({"error": E}), 500)

        return response

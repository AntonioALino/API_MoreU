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


def get_clientes():
    try:
        with Session(engine) as session:

            clientes = select(Clientes)

            jsonClientes = []

            for cliente in session.scalars(clientes):
                jsonClientes.append({
                    "id": int(cliente.id),
                    "nome": str(cliente.nome),
                    "email": str(cliente.email),
                    "contato": str(cliente.contato),
                    "nomeEmpresa": str(cliente.nomeEmpresa)

                })
            response = make_response(
                jsonify(jsonClientes), 200

            )
            response.headers["Content-Type"] = "application/json"

            return response

    except OSError:
        response = make_response(
            jsonify({"error": OSError}), 500

        )
        response.headers["Content-Type"] = "application/json"

        return response


def createClientes(form):
    form_get = loads(form)
    with Session(engine) as session:
        password = form_get["password"].encode("utf8")
        salt = gensalt()
        hash = hashpw(password, salt)

        cliente = Clientes(nome=form_get["nome"],
                           email=form_get["email"],
                           contato=form_get["contato"],
                           nomeEmpresa=form_get["nomeEmpresa"],
                           password=hash)

        session.add(cliente)
        try:
            session.commit()

            token = encode({"userId": str(cliente.id)}, os.environ.get("JWT_SECRET"))
            response = make_response(jsonify({"token": token}), 201)
            response.headers["Content-Type"] = "application/json"

            return response
        except IntegrityError:
            session.rollback()
            return make_response({"error": "This email is already being used"}, 409)


def excluirClientes(idCliente):
    try:
        with Session(engine) as session:

            delete_itens = delete(Clientes).where(Clientes.id == idCliente)

            exec_del = session.execute(delete_itens)

            session.commit()

            if (exec_del.rowcount == 0):
                return make_response("", 204)

            response = make_response("", 200)
            response.headers["Content-Type"] = "application/json"

            return response

    except OSError:
        response = make_response(
            jsonify({"error": OSError}), 500

        )
        response.headers["Content-Type"] = "application/json"

        return response


def updateClientes(form, user):
    form_get = loads(form)
    try:
        with Session(engine) as session:
            update_itens = (
                update(Clientes)
                .where(Clientes.id == user)
                .values(nome=form_get['nome'],
                        email=form_get['email'],
                        contato=form_get['contato'],
                        nomeEmpresa=form_get['nomeEmpresa']))

        exec_up = session.execute(update_itens)
        session.commit()

        if (exec_up.rowcount == 0):
            return make_response("", 204)

        response = make_response(
            "", 200
        )
        return response
    

    except IntegrityError:
        session.rollback()

        return make_response("", 409)


    except OSError:
        response = make_response(
            jsonify({"error": OSError}), 500

        )
        response.headers["Content-Type"] = "application/json"

        return response


def login(data):
    login_data = loads(data)
    try:
        with Session(engine) as session:
            queryRecept = select(Clientes).where(Clientes.email == login_data["email"])

            exec_select = session.execute(queryRecept).first()

            if exec_select:
                password = login_data["password"].encode("utf-8")
                if checkpw(password, exec_select[0].password.encode("utf-8")):

                    token = encode({"userId": str(exec_select[0].id)}, os.environ.get("JWT_SECRET"))


                    response = make_response(jsonify({"token": token}), 200)

                else:
                    response = make_response("", 401)

            else:
                response = make_response("", 204)

        return response

    except OSError:
        response = make_response(
            jsonify({"error": OSError}), 500

        )
        response.headers["Content-Type"] = "application/json"

        return response


def getClienteById(id):

    try:
        with Session(engine) as session:
            query = select(Clientes).where(Clientes.id == id)

            exec = session.execute(query).first()

            if exec:
                response = make_response(jsonify({"nomeUsuario": exec[0].nome}), 200)

            else:
                response = make_response("", 204)

            return response

    except Exception as E:
        response = make_response(jsonify({"error": E}), 500)

        return response

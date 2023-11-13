from flask import make_response, jsonify
from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update, and_
from Models.schema import Ativos
from Models.database import engine
from json import loads


def get_ativos(id):
    try:
        with Session(engine) as session:

            ativos = select(Ativos).where(Ativos.fk_id_clientes == id)

            jsonAtivos = []

            for ativo in session.scalars(ativos):
                jsonAtivos.append({
                    "id": int(ativo.id),
                    "dataCadastroProduto": str(ativo.dataCadastroProduto),
                    "nomeProduto": str(ativo.nomeProduto),
                    "qntProduto": int(ativo.qntProduto),
                    "valorPagoProduto": float(ativo.valorPagoProduto),
                    "tipoProduto": str(ativo.tipoProduto),
                    "descricaoProduto": str(ativo.descricaoProduto)

                })
            response = make_response(
                jsonify(jsonAtivos), 200

            )
            response.headers["Content-Type"] = "application/json"

            return response

    except OSError:
        response = make_response(
            jsonify({"error": OSError}), 500

        )
        response.headers["Content-Type"] = "application/json"

        return response


def createAtivos(form, id):
    form_get = loads(form)
    try:
        with Session(engine) as session:

            ativos = Ativos(dataCadastroProduto=form_get["dataCadastroProduto"],
                            nomeProduto=form_get["nomeProduto"],
                            qntProduto=form_get["qntProduto"],
                            valorPagoProduto=form_get["valorPagoProduto"],
                            tipoProduto=form_get["tipoProduto"],
                            descricaoProduto=form_get["descricaoProduto"],
                            fk_id_clientes=id)
            session.add(ativos)
            session.commit()
            response = make_response(
                "", 201

            )
        response.headers["Content-Type"] = "application/json"

        return response

    except OSError:
        response = make_response(
            jsonify({"error": OSError}), 500

        )
        response.headers["Content-Type"] = "application/json"

        return response


def excluirAtivos(idAtivo, id):
    try:
        with Session(engine) as session:

            delete_itens = delete(Ativos).where(and_(
                Ativos.id == idAtivo,
            Ativos.fk_id_clientes == id
            ))

            exec_del = session.execute(delete_itens)

            session.commit()

            if (exec_del.rowcount == 0):
                return make_response("", 204)

            response = make_response(
                "", 200

            )
            response.headers["Content-Type"] = "application/json"

            return response

    except OSError:
        response = make_response(
            jsonify({"error": OSError}), 500

        )
        response.headers["Content-Type"] = "application/json"

        return response


def updateAtivos(form, id):
    form_get = loads(form)
    try:
        with Session(engine) as session:
            update_itens = (
                update(Ativos)
                .where(and_(Ativos.id == form_get['id'], Ativos.fk_id_clientes == id))
                .values(dataCadastroProduto=form_get["dataCadastroProduto"],
                        nomeProduto=form_get['nomeProduto'],
                        qntProduto=form_get['qntProduto'],
                        valorPagoProduto=form_get["valorPagoProduto"],
                        tipoProduto=form_get['tipoProduto'],
                        descricaoProduto=form_get['descricaoProduto']))

        exec_up = session.execute(update_itens)
        session.commit()

        if (exec_up.rowcount == 0):
            return make_response("", 204) 

        return make_response("", 200)

    except OSError:
        response = make_response(
            jsonify({"error": OSError}), 500

        )
        response.headers["Content-Type"] = "application/json"

        return response


def selectById(id, idUser):
    try:
        with Session(engine) as session:
            queryRecept = select(Ativos).where(and_(Ativos.id == id, Ativos.fk_id_clientes == idUser))

        exec_select = session.execute(queryRecept).first()

        if not exec_select:
            return make_response("", 204)

        else:

            response = make_response(
                jsonify({
                    "id": int(exec_select[0].id),
                    "dataCadastroProduto": str(exec_select[0].dataCadastroProduto),
                    "nomeProduto": str(exec_select[0].nomeProduto),
                    "qntProduto": int(exec_select[0].qntProduto),
                    "valorPagoProduto": float(exec_select[0].valorPagoProduto),
                    "tipoProduto": str(exec_select[0].tipoProduto),
                    "descricaoProduto": str(exec_select[0].descricaoProduto)
                }), 200
            )
            return response

    except OSError:
        response = make_response(
            jsonify({"error": OSError}), 500

        )

        return response

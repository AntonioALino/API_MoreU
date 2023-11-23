# Importando bibliotecas necessárias do Flask
from flask import make_response, jsonify

# Importando classes e métodos necessários do SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update, and_

# Importando classes de modelo definidas no arquivo 'schema.py'
from Models.schema import Ativos, Clientes

# Importando o objeto de conexão do SQLAlchemy definido no arquivo 'database.py'
from Models.database import engine

# Importando a função 'loads' do módulo 'json'
from json import loads

# Função para obter os ativos de um cliente pelo ID do cliente
def get_ativos(id):
    try:
        with Session(engine) as session:
            # Consulta para obter ativos associados a um cliente específico
            ativos = select(Ativos).where(Ativos.fk_id_clientes == id)
            jsonAtivos = []

            # Itera sobre os resultados da consulta e cria uma lista de dicionários
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
            # Cria uma resposta HTTP com os ativos em formato JSON
            response = make_response(
                jsonify(jsonAtivos), 200

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

# Função para criar um novo ativo para um cliente
def createAtivos(form, id):
    form_get = loads(form)
    try:
        with Session(engine) as session:
            # Cria uma instância da classe Ativos com os dados fornecidos
            ativos = Ativos(dataCadastroProduto=form_get["dataCadastroProduto"],
                            nomeProduto=form_get["nomeProduto"],
                            qntProduto=form_get["qntProduto"],
                            valorPagoProduto=form_get["valorPagoProduto"],
                            tipoProduto=form_get["tipoProduto"],
                            descricaoProduto=form_get["descricaoProduto"],
                            fk_id_clientes=id)
            
            # Adiciona o novo ativo à sessão e realiza o commit para persistir no banco de dados
            session.add(ativos)
            session.commit()

            # Retorna uma resposta HTTP com status 201 (Criado)
            response = make_response(
                "", 201

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

# Função para excluir um ativo com base no ID do ativo e no ID do cliente
def excluirAtivos(idAtivo, id):
    try:
        with Session(engine) as session:

            # Cria uma instrução DELETE para excluir o ativo específico
            delete_itens = delete(Ativos).where(and_(
                Ativos.id == idAtivo
            ))

            # Executa a instrução DELETE
            exec_del = session.execute(delete_itens)

            # Realiza o commit para persistir as alterações no banco de dados
            session.commit()

            # Verifica se algum ativo foi excluído e retorna a resposta apropriada
            if (exec_del.rowcount == 0):
                return make_response("", 204)

            response = make_response(
                "", 200

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

# Função para atualizar os dados de um ativo com base no formulário e no ID do cliente
def updateAtivos(form, id):
    form_get = loads(form)
    try:
        with Session(engine) as session:
            # Cria uma instrução UPDATE para atualizar os dados do ativo específico
            update_itens = (
                update(Ativos)
                .where(and_(Ativos.id == form_get['id'], Ativos.fk_id_clientes == id))
                .values(dataCadastroProduto=form_get["dataCadastroProduto"],
                        nomeProduto=form_get['nomeProduto'],
                        qntProduto=form_get['qntProduto'],
                        valorPagoProduto=form_get["valorPagoProduto"],
                        tipoProduto=form_get['tipoProduto'],
                        descricaoProduto=form_get['descricaoProduto']))
        # Executa a instrução UPDATE
        exec_up = session.execute(update_itens)

        # Realiza o commit para manter as alterações no banco de dados
        session.commit()

        # Verifica se algum ativo foi atualizado e retorna a resposta apropriada
        if (exec_up.rowcount == 0):
            return make_response("", 204) 

        return make_response("", 200)

    except OSError:
        # Em caso de erro, retorna uma resposta de erro com status 500
        response = make_response(
            jsonify({"error": OSError}), 500

        )
        response.headers["Content-Type"] = "application/json"

        return response

# Função para obter os detalhes de um ativo com base no ID do ativo e no ID do cliente
def selectById(id, idUser):
    try:
        with Session(engine) as session:
            # Cria uma instrução SELECT para obter os detalhes do ativo específico
            queryRecept = select(Ativos).where(and_(Ativos.id == id, Ativos.fk_id_clientes == idUser))

        # Executa a instrução SELECT
        exec_select = session.execute(queryRecept).first()

        # Verifica se o ativo foi encontrado e retorna a resposta apropriada
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
        # Em caso de erro, retorna uma resposta de erro com status 500
        response = make_response(
            jsonify({"error": OSError}), 500

        )

        return response

from flask import make_response, jsonify
from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update
from Models.schema import Ativos
from Models.database import engine
from json import loads

def get_ativos(): 
  try:
   with Session(engine) as session:
 
     ativos = select(Ativos)

     jsonAtivos = []

     for ativo in session.scalars(ativos):
       jsonAtivos.append({
        "id": int(ativo.id),
        "nomeProduto": str(ativo.nomeProduto),
        "qntProduto": int(ativo.qntProduto),
        "tipoProduto": str(ativo.tipoProduto),
        "descricaoProduto": str(ativo.descricaoProduto)
       
       })
     response = make_response (
      jsonify(jsonAtivos),
        
     )
     response.headers["Content-Type"] = "application/json"

     return response
  
  except OSError:
    response = make_response (
       jsonify({"error": OSError}), 500

     )
    response.headers["Content-Type"] = "application/json"

    return response

def createAtivos(form):
  form_get = loads(form)
  try:
   with Session(engine) as session:
 
     ativos = Ativos(nomeProduto = form_get["nomeProduto"], qntProduto = form_get["qntProduto"], tipoProduto=form_get["tipoProduto"], descricaoProduto=form_get["descricaoProduto"])
     session.add(ativos)
     session.commit()
     response = make_response (
       jsonify({"created" : True}), 201

     )
   response.headers["Content-Type"] = "application/json"

   return response

  except OSError:
    response = make_response (
       jsonify({"error": OSError}), 500

     )
    response.headers["Content-Type"] = "application/json"

    return response
  
def excluirAtivos(idAtivo):
  try:
   with Session(engine) as session:
 
     delete_itens = delete(Ativos).where(Ativos.id == idAtivo)

     exec_del = session.execute(delete_itens)

     session.commit()

     response = make_response (
      jsonify({'affectedRows': exec_del.rowcount}), 202
        
     )
     response.headers["Content-Type"] = "application/json"

     return response
  
  except OSError:
    response = make_response (
       jsonify({"error": OSError}), 500

     )
    response.headers["Content-Type"] = "application/json"

    return response
  
def updateAtivos(form):
  form_get = loads(form)
  try:
    with Session(engine) as session:
      update_itens = (
      update(Ativos)
      .where(Ativos.id == form_get['id'])
      .values(nomeProduto = form_get['nomeProduto'], 
              qntProduto = form_get['qntProduto'], 
              tipoProduto = form_get['tipoProduto'], 
              descricaoProduto = form_get['descricaoProduto']))
    
    exec_up = session.execute(update_itens)
    session.commit()
    
    response = make_response(
      jsonify({'affectedRows': exec_up.rowcount}), 200
    )
    return response

  except OSError:
    response = make_response (
       jsonify({"error": OSError}), 500

     )
    response.headers["Content-Type"] = "application/json"

    return response
  

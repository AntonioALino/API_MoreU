from flask import make_response, jsonify
from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update
from Models.schema import Fornecedores
from Models.database import engine
from json import loads

def get_fornecedores(): 
  try:
   with Session(engine) as session:
 
     fornecedores = select(Fornecedores)

     jsonfornecedores = []

     for fornecedor in session.scalars(fornecedores):
       jsonfornecedores.append({
        "id": int(Fornecedores.id),
        "nomeFornecedor": str(fornecedor.nomeFornecedores),
        "emailFornecedor": str(fornecedor.emailFornecedores),
        "contatoFornecedor": str(fornecedor.contatoFornecedores),
        "nomeEmpresaFornecedor": str(fornecedor.nomeEmpresaFornecedores),
        "tipoProdutosFornecidos": str(fornecedor.tipoProdutosFornecidos),
        "qntProdutosFornecidos": int(fornecedor.qntProdutosFornecidos)
       })
     response = make_response (
      jsonify(jsonfornecedores),
        
     )
     response.headers["Content-Type"] = "application/json"

     return response
  
  except OSError:
    response = make_response (
       jsonify({"error": OSError}), 500

     )
    response.headers["Content-Type"] = "application/json"

    return response

def createfornecedores(form):
  form_get = loads(form)
  try:
   with Session(engine) as session:
 
     fornecedor = Fornecedores(
       nomeFornecedor = form_get["nomeFornecedor"], 
       emailFornecedor = form_get["emailFornecedor"], 
       contatoFornecedor=form_get["contatoFornecedor"], 
       nomeEmpresaFornecedor=form_get["nomeEmpresaFornecedor"],
       tipoProdutosFornecidos=form_get["tipoProdutosFornecidos"],
       qntProdutosFornecidos=int(form_get["qntProdutosFornecidos"]))
     
     session.add(fornecedor)
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
  
def excluirfornecedores(idfornecedor):
  try:
   with Session(engine) as session:
 
     delete_itens = delete(Fornecedores).where(Fornecedores.id == idfornecedor)

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
  
def updatefornecedores(form):
  form_get = loads(form)
  try:
    with Session(engine) as session:
      update_itens = (
      update(Fornecedores)
      .where(Fornecedores.id == form_get['id'])
      .values(nomeFornecedor = form_get['nomeFornecedor'], 
              emailFornecedor = form_get['emailFornecedor'], 
              contatoFornecedor = form_get['contatoFornecedor'], 
              nomeEmpresaFornecedor = form_get['nomeEmpresaFornecedor'],
              tiposProdutosFornecidos=form_get["tiposProdutosFornecidos"],
              qntProdutosFornecidos=form_get["qntProdutosFornecidos"]))
    
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
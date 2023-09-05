from flask import make_response, jsonify
from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update
from Models.schema import Clientes
from Models.database import engine
from json import loads

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
     response = make_response (
      jsonify(jsonClientes),
        
     )
     response.headers["Content-Type"] = "application/json"

     return response
  
  except OSError:
    response = make_response (
       jsonify({"error": OSError}), 500

     )
    response.headers["Content-Type"] = "application/json"

    return response

def createClientes(form):
  form_get = loads(form)
  try:
   with Session(engine) as session:
 
     cliente = Clientes(nome = form_get["nome"], 
                        email = form_get["email"], 
                        contato=form_get["contato"], 
                        nomeEmpresa=form_get["nomeEmpresa"])
     
     session.add(cliente)
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
  
def excluirClientes(idCliente):
  try:
   with Session(engine) as session:
 
     delete_itens = delete(Clientes).where(Clientes.id == idCliente)

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
  
def updateClientes(form):
  form_get = loads(form)
  try:
    with Session(engine) as session:
      update_itens = (
      update(Clientes)
      .where(Clientes.id == form_get['id'])
      .values(nome = form_get['nome'], 
              email = form_get['email'], 
              contato = form_get['contato'], 
              nomeEmpresa = form_get['nomeEmpresa']))
    
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
  

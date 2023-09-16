from flask import abort, make_response, jsonify
from sqlalchemy.orm import Session
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
  with Session(engine) as session:
     password = form_get["password"].encode("utf8")
     salt = gensalt()
     hash = hashpw(password, salt)
 
     cliente = Clientes(nome = form_get["nome"], 
                        email = form_get["email"], 
                        contato=form_get["contato"], 
                        nomeEmpresa=form_get["nomeEmpresa"],
                        password = hash)
     
     session.add(cliente)
     try:
      session.commit()
      response = make_response (
        jsonify({"created" : True}), 201

      )
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
  
  
def login(email, password):
  try:
    with Session(engine) as session:
      queryRecept = select(Clientes).where(Clientes.email == email)
    
    exec_select = session.execute(queryRecept).first()

    if (exec_select.count > 0):
      if (exec_select[0].password):
        pass
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
    response = make_response (
       jsonify({"error": OSError}), 500

     )
    response.headers["Content-Type"] = "application/json"

    return response
  

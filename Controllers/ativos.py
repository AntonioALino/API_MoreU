from flask import make_response, jsonify, request 
from sqlalchemy.orm import Session
from Models.schema import Ativos
from Models.database import engine

def get_ativos(): 
  try:
   with Session(engine) as session:
 
     ativos = Ativos(nomeProduto = 'Computador',qntProduto= 10, tipoProduto='Eletrônico', descricaoProduto='Computador para uso dos desenvolvedores do MoreU')
     session.add(ativos)
     session.commit()
   return make_response (
    jsonify({"created" : True}), 201

    )
  
  except OSError:
    return make_response(
      jsonify({"error": {OSError}})
    )

def createAtivos(form):
  form
  try:
   with Session(engine) as session:
 
     ativos = Ativos(nomeProduto = form.get("nomeProduto"),qntProduto= form.get("qntProduto"), tipoProduto=form.get("tipoProduto"), descricaoProduto=form.get("descricaoProduto"))
     session.add(ativos)
     session.commit()
   return make_response (
    jsonify({"created" : True}), 201

    )
  
  except OSError:
    return make_response(
      jsonify({"error": {OSError}})
    )
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

class Ativos(Base):

  def __init__(self ,nomeProduto , qntProduto , tipoProduto, descricaoProduto):
    self.nomeProduto = nomeProduto
    self.qntProduto = qntProduto
    self.tipoProduto = tipoProduto
    self.descricaoProduto = descricaoProduto

  __tablename__ = 'ativos'
  id = Column(Integer, primary_key= True, autoincrement=True)
  nomeProduto = Column("nomeProduto", String(60))
  qntProduto = Column("qntProduto", Integer)
  tipoProduto = Column("tipoProduto", String(60))
  descricaoProduto = Column("descricaoProduto", String(60))

  def __repr__(self) -> str:
    return f"User(id={self.id!r}, name={self.nomeProduto!r}, type={self.tipoProduto!r})"

class Clientes(Base):
  __tablename__ = 'clientes'
  id = Column(Integer, primary_key= True, autoincrement=True)
  nome = Column(String(60))
  email = Column(String(30))
  contato = Column(Integer)
  nomeEmpresa = Column(String(60))
  def __init__(self, nome = None, email = None, contato = None, nomeEmpresa = None):
    self.nome = nome
    self.email = email
    self.contato = contato
    self.nomeEmpresa = nomeEmpresa
class Fornecedores(Base):

  def __init__(self, nomeFornecedor = None, emailFornecedor = None, contatoFornecedor = None, nomeEmpresaFornecedor = None, tipoProdutosFornecidos = None,qntProdutosFornecidos = None,):
    self.nomeFornecedor= nomeFornecedor
    self.emailFornecedor= emailFornecedor
    self.contatoFornecedor = contatoFornecedor
    self.nomeEmpresaFornecedor = nomeEmpresaFornecedor
    self.tipoProdutosFornecidos = tipoProdutosFornecidos
    self.qntProtudosFornecidos = qntProdutosFornecidos
    
  __tablename__ = 'fornecedores'
  id = Column(Integer, primary_key= True, autoincrement=True)
  nomeFornecedor = Column(String(60))
  emailFornecedor = Column(String(30))
  contatoFornecedor = Column(Integer)
  nomeEmpresaFornecedor = Column(String(60))
  tipoProdutosFornecidos = Column(String(60))
  qntProdutosFornecidos = Column(Integer)

from sqlalchemy import Integer, Double, String, Date, Column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Ativos(Base):

    def __init__(self, dataCadastroProduto, nomeProduto, qntProduto, valorPagoProduto, tipoProduto, descricaoProduto):
        self.dataCadastroProduto = dataCadastroProduto
        self.nomeProduto = nomeProduto
        self.qntProduto = qntProduto
        self.valorPagoProduto = valorPagoProduto
        self.tipoProduto = tipoProduto
        self.descricaoProduto = descricaoProduto

    __tablename__ = 'ativos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dataCadastroProduto = Column("dataCadastroProduto", Date)
    nomeProduto = Column("nomeProduto", String(60))
    qntProduto = Column("qntProduto", Integer)
    valorPagoProduto = Column("valorPagoProduto", Double)
    tipoProduto = Column("tipoProduto", String(60))
    descricaoProduto = Column("descricaoProduto", String(60))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.nomeProduto!r}, type={self.tipoProduto!r})"


class Clientes(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60))
    email = Column(String(30), unique=True)
    contato = Column(String(11))
    nomeEmpresa = Column(String(60))
    password = Column(String(200))

    def __init__(self, nome=None, email=None, contato=None, nomeEmpresa=None, password=None):
        self.nome = nome
        self.email = email
        self.contato = contato
        self.nomeEmpresa = nomeEmpresa
        self.password = password

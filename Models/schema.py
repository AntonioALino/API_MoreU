# Importando as bibliotecas necessárias do SQLAlchemy
from sqlalchemy import Integer, Double, String, Date, Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship

# Criando uma classe base para herança de modelo declarativo
class Base(DeclarativeBase):
    pass

# Definindo a classe para a tabela 'ativos'
class Ativos(Base):
    # Inicializador da classe
    def __init__(self, dataCadastroProduto, nomeProduto, qntProduto, valorPagoProduto, tipoProduto, descricaoProduto, fk_id_clientes):
        self.dataCadastroProduto = dataCadastroProduto
        self.nomeProduto = nomeProduto
        self.qntProduto = qntProduto
        self.valorPagoProduto = valorPagoProduto
        self.tipoProduto = tipoProduto
        self.descricaoProduto = descricaoProduto
        self.fk_id_clientes = fk_id_clientes

    # Nome da tabela no banco de dados
    __tablename__ = 'ativos'

    # Definindo colunas da tabela 'ativos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dataCadastroProduto = Column("dataCadastroProduto", Date)
    nomeProduto = Column("nomeProduto", String(60))
    qntProduto = Column("qntProduto", Integer)
    valorPagoProduto = Column("valorPagoProduto", Double)
    tipoProduto = Column("tipoProduto", String(60))
    descricaoProduto = Column("descricaoProduto", String(60))
    fk_id_clientes = Column(ForeignKey("clientes.id"))
    # Criando relação com a tabela 'clientes'
    cliente = relationship("Clientes")

    # Representação string da instância da classe
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.nomeProduto!r}, type={self.tipoProduto!r})"

# Definindo a classe para a tabela 'clientes'
class Clientes(Base):
    # Nome da tabela no banco de dados
    __tablename__ = 'clientes'

    # Definindo colunas da tabela 'clientes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60))
    email = Column(String(30), unique=True)
    contato = Column(String(11))
    nomeEmpresa = Column(String(60))
    password = Column(String(200))

    # Inicializador da classe
    def __init__(self, nome=None, email=None, contato=None, nomeEmpresa=None, password=None):
        self.nome = nome
        self.email = email
        self.contato = contato
        self.nomeEmpresa = nomeEmpresa
        self.password = password

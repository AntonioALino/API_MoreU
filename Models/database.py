# Importando as bibliotecas necessárias
from sqlalchemy import create_engine
from dotenv import load_dotenv, find_dotenv
import os

# Carregando variáveis de ambiente do arquivo .env
load_dotenv(find_dotenv())

# Criando uma conexão com o banco de dados usando a URL fornecida no arquivo .env
engine = create_engine(os.environ.get("URL"), echo=True)

from sqlalchemy import create_engine
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


engine = create_engine(os.environ.get("URL"), echo=True)

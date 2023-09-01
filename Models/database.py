# from flask import Flask, make_response, jsonify, request
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

env = load_dotenv(".env")

engine = create_engine(os.environ.get('URL'), echo=True)


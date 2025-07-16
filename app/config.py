from flask_jwt_extended import JWTManager
from sqlalchemy import select, exists
from flask import Flask
import os

from database import Database
from models import *

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'default_secret_key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 86400

jwt = JWTManager(app)

HOST = os.environ.get('HOST')
PORT = int(os.environ.get('PORT'))

POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")

db = Database(POSTGRES_HOST, POSTGRES_PORT,
              POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB)

ROOT_USER = os.environ.get("ROOT_USER")
ROOT_PASSWORD_HASH = os.environ.get("ROOT_PASSWORD_HASH")

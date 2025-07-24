from flask_jwt_extended import JWTManager
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from sqlalchemy import select, exists
from flask import Flask
import os

from lib.database import Database
from lib.models import *
from lib.email import EmailSender, EmailSenderOffline

app = Flask(__name__, static_folder="../web/static", template_folder="../web/templates") # FIXME: сменить static_folder на конкретные views, в конце разработки
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

MAIL_HOST = os.environ.get("MAIL_HOST")
MAIL_PORT = int(os.environ.get("MAIL_PORT"))
MAIL_USER = os.environ.get("MAIL_USER")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_SSL = bool(os.environ.get("MAIL_SSL", False))

if any(var is None for var in [MAIL_HOST, MAIL_PORT, MAIL_USER, MAIL_PASSWORD]):
    mail = EmailSenderOffline()
else:
    mail = EmailSender(
        host=MAIL_HOST,
        port=MAIL_PORT,
        username=MAIL_USER,
        password=MAIL_PASSWORD,
        use_ssl=MAIL_SSL
    )

ROOT_USER = os.environ.get("ROOT_USER")
ROOT_PASSWORD_HASH = os.environ.get("ROOT_PASSWORD_HASH")

font_path = os.path.join(os.getcwd(), "web", "static", "Inter.ttf")
pdfmetrics.registerFont(TTFont('Inter', font_path)) 

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask import Blueprint, request
import bcrypt

from config import *

admin = Blueprint('admin', __name__, url_prefix='/admin')

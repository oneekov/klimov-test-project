from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask import Blueprint, request
import bcrypt

from config import *

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/auth', methods=['POST'])
def login():
    data = request.json
    if not data:
        return {'status': 'error', 'message': 'creds not provided'}, 400
    
    username, password = data.get('username'), data.get('password') 

    if not (username and password):
        return {'status': 'error', 'message': 'creds not provided'}, 400
    
    with db.session() as session:
        user: Admin = (session.execute(select(Admin).where(Admin.username==username))).scalars().first()

    if not user:
        return {'status': 'error', 'message': 'user not exist'}, 404
    
    if bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
        return {'status': 'ok', 'token': create_access_token(user.admin_id)}
    
    return {'status': 'error', 'message': 'bad creds provided'}, 401

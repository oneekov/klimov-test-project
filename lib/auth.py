from flask_jwt_extended import create_access_token
from flask import Blueprint, request
from pydantic import ValidationError
from sqlalchemy import or_
import bcrypt

from lib.validators import UserInput
from lib.config import *

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data:
        return {'status': 'error', 'message': 'data not provided'}, 400
    
    try:
        user = UserInput(**data)
    except ValidationError as e:
        return {'status': 'error', 'message': e.errors()[0]['msg']}, 400
    
    with db.session() as session:
        result = session.execute(select(User).where(User.username==user.username))
        existing_user = result.scalars().first()
        if existing_user:
            return {'status': 'error', 'message': 'user already exists'}, 409
        created_user = User(
            username=user.username,
            password_hash=bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),

            school=user.school,
            grade_number=user.grade[0],
            grade_letter=user.grade[1],
            
            surname=user.full_name[0],
            name=user.full_name[1],
            patronymic=user.full_name[2],

            contact_email=user.email,
            contact_number=user.number,
        )
        session.add(created_user)
        session.commit()
    
    return {'status': 'ok', 'token': create_access_token(identity=str(created_user.id))}, 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data:
        return {'status': 'error', 'message': 'creds not provided'}, 400
    
    username, password = data.get('username'), data.get('password') 

    if not (username and password):
        return {'status': 'error', 'message': 'creds not provided'}, 400
    
    with db.session() as session:
        user: User = (session.execute(select(User).where(User.username==username))).scalars().first()

    if not user:
        return {'status': 'error', 'message': 'user not exist'}, 404
    
    if bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
        return {'status': 'ok', 'token': create_access_token(identity=str(user.id))}
    
    return {'status': 'error', 'message': 'bad creds provided'}, 401

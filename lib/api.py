from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import Blueprint, request
from pydantic import ValidationError

from lib.admin import admin
from lib.auth import auth
from lib.config import *

api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(admin)
api.register_blueprint(auth)

@api.route('/send_results', methods=['POST'])
@jwt_required()
def send_results():
    data = request.json
    if not data:
        return {'status': 'error', 'message': 'data not provided'}, 400
    
    if any(not key in data['results'] for key in ['nature', 'tech', 'human', 'sign_system', 'image']):
        return {'status': 'error', 'message': 'not all data provided'}, 400
    
    for key, value in data['results'].items():
        if not (-20 <= value <= 20):
            return {"status": "error", "message": "bad results provided (range -20 - 20)"}, 400
    
    
    with db.session() as session:
        result = Answer(
            ip=request.remote_addr,
            user_agent=request.headers.get('User-Agent'),

            user_id=get_jwt_identity(),
            
            nature_points=data['results']['nature'],
            tech_points=data['results']['tech'],
            human_points=data['results']['human'],
            sign_points=data['results']['sign_system'],
            image_points=data['results']['image']
        ) # notFIXME: подозреваю, что можно загонять pydantic модель в SQLAlchemy напрямую, но нужно копаться в моделях...
        # upd: ладно, пофиг
        session.add(result)
        session.commit()

    return {'status': 'ok', 'message': 'results received successfully'}, 200

@api.route('/me', methods=['GET'])
@jwt_required()
def me():
    with db.session() as session:
        user = session.query(User).filter_by(id=int(get_jwt_identity())).first()
        return {"user": {k: v for k, v in user.__dict__.items() if not k.startswith('_') and not k in ['password_hash', 'username']}}, 200

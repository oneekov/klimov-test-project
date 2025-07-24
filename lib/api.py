from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import Blueprint, request, send_file
import io
from pydantic import ValidationError

from lib.admin import admin
from lib.auth import auth
from lib.config import *
from lib.report import create_pdf_report

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

        answers = session.execute(
            select(Answer).where(Answer.user_id == int(get_jwt_identity()))
        ).scalars().all()

        # Форматирование ответов с вложенной информацией о пользователе
        formatted_answers = []
        for answer in answers:
            answer_data = {
                k: v for k, v in answer.__dict__.items() 
                if not k.startswith('_') and k not in ['user_agent', 'ip', 'user_id']
            }
            formatted_answers.append(answer_data)

        return {'user': {k: v for k, v in user.__dict__.items() if not k.startswith('_') and not k in ['password_hash', 'username']}, 'answers': formatted_answers}, 200

@api.route('/report/<int:id>', methods=['GET'])
def report(id: int):
    with db.session() as session:
        answer = session.query(Answer).filter_by(answer_id=id).first()
        if not answer:
            return {'status': 'error', 'message': 'answer not found'}, 404

        user = session.execute(
            select(User).where(User.id == answer.user_id)
        ).scalars().first()

        points = {
            'nature': answer.nature_points,
            'tech': answer.tech_points,
            'human': answer.human_points,
            'sign_system': answer.sign_points,
            'image': answer.image_points
        }

        max_points = max(points.values())
        max_keys = [k for k, v in points.items() if v == max_points]

        if len(max_keys) == 1:
            match max_keys[0]:
                case 'nature':
                    content = "работе с природой"
                case 'tech':
                    content = "технической деятельности"
                case 'human':
                    content = "работе с людьми"
                case 'sign_system':
                    content = "работе с знаковыми системами"
                case 'image':
                    content = "творческой деятельности"
        else:
            content = "разнообразной деятельности"

        pdf_data = create_pdf_report(user.surname, user.name, user.patronymic, content)

        return send_file(
            io.BytesIO(pdf_data),
            mimetype='application/pdf',
            as_attachment=True,
            download_name=f'cert_{id}.pdf'
        )

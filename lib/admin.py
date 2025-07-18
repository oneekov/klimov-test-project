from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import or_, not_, and_
from flask import Blueprint, request

from lib.config import *

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/users/', methods=['GET'])
@jwt_required()
def get_users():
    with db.session() as session:
        user = session.execute(select(User).where(User.id==int(get_jwt_identity()))).scalar()
        if not (user.is_admin or user.is_super_admin):
            return {'status': 'error', 'message': 'access denied'}, 403
        
        users = session.execute(select(User).where(not_(or_(User.is_admin, User.is_super_admin)))).scalars().all()
        formatted_users = [{k: v for k, v in i.__dict__.items() if not k.startswith('_') and not k in ['password_hash', 'username']} for i in users]
        return {'users': formatted_users}, 200

@admin.route('/admins/', methods=['GET'])
@jwt_required()
def get_admins():
    with db.session() as session:
        user = session.execute(select(User).where(User.id==int(get_jwt_identity()))).scalar()
        if not user.is_super_admin:
            return {'status': 'error', 'message': 'access denied'}, 403
        
        users = session.execute(select(User).where(or_(User.is_admin, User.is_super_admin))).scalars().all()
        formatted_users = [{k: v for k, v in i.__dict__.items() if not k.startswith('_') and not k in ['password_hash', 'username']} for i in users]
        return {'admins': formatted_users}, 200

@admin.route('/answers/', methods=['GET'])
@jwt_required()
def get_answers():
    school = request.args.get('school', None)
    grade_number = request.args.get('grade_number', None)
    profession_type = request.args.get('profession_type', None)

    with db.session() as session:
        user = session.execute(select(User).where(User.id==int(get_jwt_identity()))).scalar()
        if not (user.is_admin or user.is_super_admin):
            return {'status': 'error', 'message': 'access denied'}, 403
        
        answers = session.query(Answer)
        if school:
            answers = answers.filter(Answer.school == school)
        if grade_number:
            answers = answers.filter(Answer.grade_number == grade_number)
        if profession_type and profession_type in ['nature', 'tech', 'human', 'sign_system', 'image']:
            main_field = getattr(User, profession_type)
            other_fields = [getattr(User, f) for f in ['nature', 'tech', 'human', 'sign_system', 'image'] if f != profession_type]
    
            condition = and_(*[main_field > other for other in other_fields])
            answers = answers.filter(condition)
        
        answers = answers.all()

        formatted_answers = [{k: v for k, v in i.__dict__.items() if not k.startswith('_') and not k in ['user_agent', 'ip']} for i in answers]

        for answer in formatted_answers:
            user = session.execute(select(User).where(User.id==answer['user_id'])).scalar()
            del answer['user_id']
            answer['user'] = {k: v for k, v in user.__dict__.items() if not k.startswith('_') and not k in ['password_hash', 'username']}

    return {'answers': formatted_answers}, 200

@admin.route('/answers/csv/', methods=['GET'])
@jwt_required()
def get_answers_csv():
    school = request.args.get('school', None)
    grade_number = request.args.get('grade_number', None)
    profession_type = request.args.get('profession_type', None)

    with db.session() as session:
        user = session.execute(select(User).where(User.id==int(get_jwt_identity()))).scalar()
        if not (user.is_admin or user.is_super_admin):
            return {'status': 'error', 'message': 'access denied'}, 403
    # TODO: реализовать выгрузку в CSV

@admin.route('/answers/excel/', methods=['GET'])
@jwt_required()
def get_answers_excel():
    school = request.args.get('school', None)
    grade_number = request.args.get('grade_number', None)
    profession_type = request.args.get('profession_type', None)

    with db.session() as session:
        user = session.execute(select(User).where(User.id==int(get_jwt_identity()))).scalar()
        if not (user.is_admin or user.is_super_admin):
            return {'status': 'error', 'message': 'access denied'}, 403
    # TODO: реализовать выгрузку в Excel

@admin.route('/admins/rights', methods=['PATCH'])
def change_rights():
    #TODO: реализовать изменение прав администратора
    return {'status': 'error', 'message': 'not implemented'}, 501

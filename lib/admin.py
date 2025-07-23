from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import or_, not_, and_, case, func
from flask import Blueprint, request, send_file
from datetime import datetime
import pandas as pd
import io

from lib.config import *

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/users/', methods=['GET'])
@jwt_required()
def get_users():
    offset = int(request.args.get('offset', 0))
    limit = min(int(request.args.get('limit', 50)), 50)
    with db.session() as session:
        user = session.execute(select(User).where(User.id==int(get_jwt_identity()))).scalar()
        if not (user.is_admin or user.is_super_admin):
            return {'status': 'error', 'message': 'access denied'}, 403
        
        users = session.execute(select(User).where(not_(or_(User.is_admin, User.is_super_admin))).offset(offset).limit(limit)).scalars().all()
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
    offset = int(request.args.get('offset', 0))
    limit = min(int(request.args.get('limit', 50)), 50)

    with db.session() as session:
        user = session.execute(select(User).where(User.id==int(get_jwt_identity()))).scalar()
        if not (user.is_admin or user.is_super_admin):
            return {'status': 'error', 'message': 'access denied'}, 403
        
        answers_query = session.query(Answer).join(User, Answer.user_id == User.id)

        # Фильтрация по school и grade_number
        if school is not None:
            answers_query = answers_query.filter(User.school.ilike(f'%{school}%'))
        if grade_number is not None:
            answers_query = answers_query.filter(User.grade_number == grade_number)

        if profession_type and profession_type in ['nature', 'tech', 'human', 'sign_system', 'image']:
            main_field = getattr(User, profession_type)
            other_fields = [getattr(User, f) for f in ['nature', 'tech', 'human', 'sign_system', 'image'] if f != profession_type]
    
            condition = and_(*[main_field > other for other in other_fields])
            answers = answers.filter(condition)
        
        answers = answers.offset(offset).limit(limit).all()

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

    # Преобразование grade_number в int, если задано
    if grade_number is not None:
        try:
            grade_number = int(grade_number)
        except ValueError:
            return {'status': 'error', 'message': 'grade_number must be an integer'}, 400

    with db.session() as session:
        # Получаем текущего пользователя
        user = session.execute(select(User).where(User.id == int(get_jwt_identity()))).scalar()
        if not (user.is_admin or user.is_super_admin):
            return {'status': 'error', 'message': 'access denied'}, 403

        # Начинаем запрос к Answer с JOIN по User
        answers_query = session.query(Answer).join(User, Answer.user_id == User.id)

        # Фильтрация по school и grade_number
        if school is not None:
            answers_query = answers_query.filter(User.school.ilike(f'%{school}%'))
        if grade_number is not None:
            answers_query = answers_query.filter(User.grade_number == grade_number)

        # Фильтрация по profession_type (если указан)
        if profession_type and profession_type in ['nature', 'tech', 'human', 'sign_system', 'image']:
            main_field = getattr(User, profession_type + '_points')  # Предполагаем, что есть поля типа nature_points
            other_fields = [getattr(User, f + '_points') for f in ['nature', 'tech', 'human', 'sign_system', 'image'] if f != profession_type]
            condition = and_(*[main_field > other for other in other_fields])
            answers_query = answers_query.filter(condition)

        # Выполняем запрос и форматируем данные
        answers = answers_query.all()
        formatted_answers = [a.__dict__ for a in answers]

        # Добавляем информацию о пользователе в каждый ответ
        for answer in formatted_answers:
            user = session.execute(select(User).where(User.id == answer['user_id'])).scalar()
            del answer['user_id']
            answer['user'] = user.__dict__

    # Формируем CSV-файл
    data = []
    for answer in formatted_answers:
        user = answer['user']
        data.append({
            "Фамилия": user.get('surname'),
            "Имя": user.get('name'),
            "Отчество": user.get('patronymic'),
            "Класс": user.get('grade_number'),
            "Школа": user.get('school'),
            "Почта": user.get('contact_email'),
            "Номер": user.get('contact_number'),
            "Ч-П": answer.get('nature_points'),
            "Ч-Т": answer.get('tech_points'),
            "Ч-Ч": answer.get('human_points'),
            "Ч-ЗС": answer.get('sign_points'),
            "Ч-ИО": answer.get('image_points')
        })

    df = pd.DataFrame(data)
    csv_data = io.BytesIO()
    df.to_csv(csv_data, index=False, encoding='utf-8-sig')
    csv_data.seek(0)

    return send_file(
        csv_data,
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'Answers-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.csv'
    )

@admin.route('/answers/excel/', methods=['GET'])
@jwt_required()
def get_answers_excel():
    school = request.args.get('school', None)
    grade_number = request.args.get('grade_number', None)
    profession_type = request.args.get('profession_type', None)

    # Преобразование grade_number в int, если задано
    if grade_number is not None:
        try:
            grade_number = int(grade_number)
        except ValueError:
            return {'status': 'error', 'message': 'grade_number must be an integer'}, 400

    with db.session() as session:
        # Получаем текущего пользователя
        user = session.execute(select(User).where(User.id == int(get_jwt_identity()))).scalar()
        if not (user.is_admin or user.is_super_admin):
            return {'status': 'error', 'message': 'access denied'}, 403

        # Начинаем запрос к Answer с JOIN по User
        answers_query = session.query(Answer).join(User, Answer.user_id == User.id)

        # Фильтрация по school и grade_number
        if school is not None:
            answers_query = answers_query.filter(User.school.ilike(f'%{school}%'))
        if grade_number is not None:
            answers_query = answers_query.filter(User.grade_number == grade_number)

        # Фильтрация по profession_type (если указан)
        if profession_type and profession_type in ['nature', 'tech', 'human', 'sign_system', 'image']:
            main_field = getattr(User, profession_type + '_points')  # Предполагаем, что есть поля типа nature_points
            other_fields = [getattr(User, f + '_points') for f in ['nature', 'tech', 'human', 'sign_system', 'image'] if f != profession_type]
            condition = and_(*[main_field > other for other in other_fields])
            answers_query = answers_query.filter(condition)

        # Выполняем запрос и форматируем данные
        answers = answers_query.all()
        formatted_answers = [a.__dict__ for a in answers]

        # Добавляем информацию о пользователе в каждый ответ
        for answer in formatted_answers:
            user = session.execute(select(User).where(User.id == answer['user_id'])).scalar()
            del answer['user_id']
            answer['user'] = user.__dict__

    data = []
    for answer in formatted_answers:
        data.append({
                "Фамилия": answer['user']['surname'],
                "Имя": answer['user']['name'],
                "Отчество": answer['user']['patronymic'],
                "Класс": answer['user']['grade_number'],
                "Школа": answer['user']['school'],
                "Почта": answer['user']['contact_email'],
                "Номер": answer['user']['contact_number'],
                "Ч-П": answer['nature_points'],
                "Ч-Т": answer['tech_points'],
                "Ч-Ч": answer['human_points'],
                "Ч-ЗС": answer['sign_points'],
                "Ч-ИО": answer['image_points']
        })
    
    df = pd.DataFrame(data)
    excel_data = io.BytesIO()
    with pd.ExcelWriter(excel_data, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

    excel_data.seek(0)

    return send_file(
        excel_data,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name=f'Answers-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.xlsx'
    )

@admin.route('/answers/stats', methods=['GET'])
@jwt_required()
def get_answers_stats():
    school = request.args.get('school', None)
    grade_number = request.args.get('grade_number', None)

    with db.session() as session:
        user_id = get_jwt_identity()
        user = session.execute(
            select(User).where(User.id == int(user_id))
        ).scalar()

        if not (user.is_admin or user.is_super_admin):
            return {'status': 'error', 'message': 'access denied'}, 403

        # Базовый запрос
        base_query = session.query(Answer).join(User, Answer.user_id == User.id)

        # Фильтрация по school и grade_number
        if school is not None:
            base_query = base_query.filter(User.school.ilike(f'%{school}%'))
        if grade_number is not None:
            base_query = base_query.filter(User.grade_number == grade_number)

        # Определяем CASE для определения категории
        category_case = case(
                (and_(
                    Answer.nature_points > Answer.tech_points,
                    Answer.nature_points > Answer.human_points,
                    Answer.nature_points > Answer.sign_points,
                    Answer.nature_points > Answer.image_points
                ), 'nature'),
                (and_(
                    Answer.tech_points > Answer.nature_points,
                    Answer.tech_points > Answer.human_points,
                    Answer.tech_points > Answer.sign_points,
                    Answer.tech_points > Answer.image_points
                ), 'tech'),
                (and_(
                    Answer.human_points > Answer.nature_points,
                    Answer.human_points > Answer.tech_points,
                    Answer.human_points > Answer.sign_points,
                    Answer.human_points > Answer.image_points
                ), 'human'),
                (and_(
                    Answer.sign_points > Answer.nature_points,
                    Answer.sign_points > Answer.tech_points,
                    Answer.sign_points > Answer.human_points,
                    Answer.sign_points > Answer.image_points
                ), 'sign_system'),
                (and_(
                    Answer.image_points > Answer.nature_points,
                    Answer.image_points > Answer.tech_points,
                    Answer.image_points > Answer.human_points,
                    Answer.image_points > Answer.sign_points
                ), 'image'),
            
            else_='undefined'
        ).label('category')

        # Группируем по категории и считаем количество
        stats_query = base_query.with_entities(
            category_case,
            func.count(Answer.answer_id).label('count')
        ).group_by(category_case)

        # Выполняем запрос
        stats_results = stats_query.all()

        # Инициализируем словарь статистики
        stats = {
            'nature': 0,
            'tech': 0,
            'human': 0,
            'sign_system': 0,
            'image': 0,
            'undefined': 0
        }

        # Обновляем значения
        for category, count in stats_results:
            if category in stats:
                stats[category] = count
            else:
                stats['undefined'] += count

        return {'stats': stats}, 200

@admin.route('/rights/<int:id>', methods=['PATCH'])
@jwt_required()
def change_rights(id):
    if id == 1: return {'status': 'error', 'message': 'r u stupid or what'}, 403

    data = request.json
    if not data:
        return {'status': 'error', 'message': 'data not provided'}, 400

    is_admin = data.get('is_admin', None)
    is_super_admin = data.get('is_super_admin', None)

    if is_admin is None or is_super_admin is None:
        return {'status': 'error', 'message': 'data not provided'}, 400
    
    with db.session() as session:
        user = session.execute(select(User).where(User.id==int(get_jwt_identity()))).scalar()
        if not (user.is_admin or user.is_super_admin):
            return {'status': 'error', 'message': 'access denied'}, 403
        
        target_user = session.execute(select(User).where(User.id==id)).scalar()
        if not target_user:
            return {'status': 'error', 'message': 'user not found'}, 404
        
        target_user.is_admin = is_admin
        target_user.is_super_admin = is_super_admin
        session.commit()

        return {'status': 'ok', 'message': 'rights updated successfully'}, 200

@admin.route('/user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_and_answers(user_id):
    with db.session() as session:
        # Проверка прав текущего пользователя
        current_user = session.execute(
            select(User).where(User.id == int(get_jwt_identity()))
        ).scalar()
        if not (current_user.is_admin or current_user.is_super_admin):
            return {'status': 'error', 'message': 'access denied'}, 403

        # Получение пользователя по ID
        user = session.execute(
            select(User).where(User.id == user_id)
        ).scalar()
        if not user:
            return {'status': 'error', 'message': 'user not found'}, 404

        # Форматирование данных пользователя
        formatted_user = {
            k: v for k, v in user.__dict__.items() 
            if not k.startswith('_') and k not in ['password_hash', 'username']
        }

        # Получение всех ответов пользователя
        answers = session.execute(
            select(Answer).where(Answer.user_id == user_id)
        ).scalars().all()

        # Форматирование ответов с вложенной информацией о пользователе
        formatted_answers = []
        for answer in answers:
            answer_data = {
                k: v for k, v in answer.__dict__.items() 
                if not k.startswith('_') and k not in ['user_agent', 'ip', 'user_id']
            }
            formatted_answers.append(answer_data)

        return {'user': formatted_user, 'answers': formatted_answers}, 200

@admin.route('/stats')
@jwt_required()
def get_stats():
    with db.session() as session:
        user = session.execute(select(User).where(User.id==int(get_jwt_identity()))).scalar()
        if not (user.is_admin or user.is_super_admin):
            return {'status': 'error', 'message': 'access denied'}, 403
        
        total_users = session.execute(select(func.count(User.id))).scalar()
        total_answers = session.execute(select(func.count(Answer.answer_id))).scalar()

        stats = {
            'total_users': total_users,
            'total_answers': total_answers
        }

    return {'stats': stats}, 200

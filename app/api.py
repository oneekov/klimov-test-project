from flask import Blueprint, request
from pydantic import ValidationError

from admin import admin
from config import *
from validators import Result

api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(admin)

# @api.route('/check_test/', defaults={'id': None})
# @api.route('/check_test/<int:id>')
# async def check_test_existence(id=None):
#     if id:
#         if id > 2**32:
#             return {'status': 'error', 'message': 'bad id provided'}, 400
        
#         async with db.session() as session:
#             if (await session.execute(select(exists().where(Test.test_id==id)))).scalar():
#                 return {'status': 'ok'}, 200

#             return {'status': 'error', 'message': 'test not found'}, 404
    
#     return {'status': 'error', 'message': 'no id provided'}, 400

@api.route('/send_results', methods=['POST'])
def send_results():
    data = request.json
    if not data:
        return {'status': 'error', 'message': 'data not provided'}, 400
    
    try:
        result = Result(**data)
    except ValidationError as e:
        return {'status': 'error', 'message': e.errors()[0]['msg']}, 400
    
    with db.session() as session:
        result = Answer(ip=request.remote_addr,
                        user_agent=request.headers.get('User-Agent'),
                        sex=SexEnum.FEMALE if result.person.sex else SexEnum.MALE,
                        age=result.person.age,
                        surname=result.person.full_name[0],
                        name=result.person.full_name[1],
                        patronymic=result.person.full_name[2],
                        nature_points=result.results.nature,
                        tech_points=result.results.tech,
                        human_points=result.results.human,
                        sign_points=result.results.sign_system,
                        image_points=result.results.image
        ) # FIXME: подозреваю, что можно загонять pydantic модель в SQLAlchemy напрямую, но нужно копаться в моделях...
        session.commit()

    return {'status': 'ok', 'message': 'results received successfully'}, 200

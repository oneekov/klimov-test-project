from config import *
from api import api

app.register_blueprint(api)


@app.route('/')
async def index():
    return 'index page' #TODO: index page

@app.route('/healthz')
async def healthz():
    return {'status': 'ok'}

@app.route('/test/', defaults={'id': None})
@app.route('/test/<int:id>')
async def test(id):
    return 'test page' #TODO: test page

if __name__ == '__main__':
    with db.session() as session:
        if not (session.execute(select(exists().where(Admin.admin_id==1)))).scalar():
            root = Admin(admin_id=1, username=ROOT_USER, password_hash=ROOT_PASSWORD_HASH, is_super_admin=True)
            session.add(root)
            session.commit()
    app.run(host=HOST, port=PORT, debug=True)

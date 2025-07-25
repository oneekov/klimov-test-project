from flask import send_from_directory, abort
from sqlalchemy import text

from lib.config import *
from lib.api import api
from lib.views import *

with db.session() as session:
    if not (session.execute(select(exists().where(User.id==1)))).scalar():
        root = User(id=1, username=ROOT_USER, password_hash=ROOT_PASSWORD_HASH, is_super_admin=True, surname="Супер", name="Админ", patronymic="Великолепный")
        session.execute(text("SELECT setval('klimov.users_id_seq', 1)"))
        session.add(root)
        session.commit()

app.register_blueprint(api)

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'front'), filename)

@app.route('/healthz')
def healthz():
    return {'status': 'ok'}

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'web', 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)

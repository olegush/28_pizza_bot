import os

from dotenv import load_dotenv
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth

load_dotenv()

FLASK_SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
ADMIN_LOGIN = os.environ.get('ADMIN_LOGIN')
ADMIN_PWD = os.environ.get('ADMIN_PWD')

from app import app, db
from models import Pizza, Choice

app.config['BASIC_AUTH_USERNAME'] = ADMIN_LOGIN
app.config['BASIC_AUTH_PASSWORD'] = ADMIN_PWD
app.secret_key = FLASK_SECRET_KEY
app.config['BASIC_AUTH_FORCE'] = True
basic_auth = BasicAuth(app)

admin = Admin(app, name='/', template_mode='bootstrap3')
admin.add_view(ModelView(Pizza, db.session))
admin.add_view(ModelView(Choice, db.session))

if __name__ == '__main__':
    host = os.environ.get('HOST')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port, use_reloader=True)

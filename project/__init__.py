import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)


app.config['SECRET_KEY'] = 'key'
app.config['UPLOAD_FOLDER'] = '/shirt_img'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"

from .contact.views import contact_blueprint
from .admin.views import admin_blueprint
from .shirts.views import shirts_blueprint

app.register_blueprint(contact_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(shirts_blueprint)


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager, make_secure_token

import os

# config 

app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_object(os.environ['APP_SETTINGS'])
#CsrfProtect(app)
db = SQLAlchemy(app)


from project.users.views import users_blueprint
from project.home.views import home_blueprint

# blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)


from models import User

login_manager.login_view = "users.login"
login_manager.session_protection = "strong"
login_manager.make_secure_token = "users.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()



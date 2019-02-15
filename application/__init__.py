# flask-sovellus
from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

# tietokanta
from flask_sqlalchemy import SQLAlchemy

import os
import psycopg2

if os.environ.get("HEROKU"):
  app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///forum.db"
  app.config["SQLALCHEMY_ECHO"] = True
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# kirjautuminen (osa 1)

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# autorisointi
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True

            if current_user.get_role == role:
              unauthorized = False

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# oman sovelluksen toiminnallisuudet
from application import views

from application.util import filters

from application.threads import models
from application.threads import views

from application.messages import models
from application.messages import views

from application.auth import models
from application.auth import views

# kirjautuminen (osa 2)
from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# luodaan taulut tietokantaan tarvittaessa
try:
  db.create_all()
except:
  pass

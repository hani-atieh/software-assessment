from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path
from sqlalchemy import *
from flask import Flask

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hani.f2s9@dYh*91uWqzP!7zX_secret.key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .gameinfo import gameinfo
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(gameinfo, url_prefix='/games to review')
    app.static_folder = 'STATIC'

    from .models import User, Review, Games


    

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
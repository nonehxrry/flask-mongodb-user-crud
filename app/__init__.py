from flask import Flask
from flask_pymongo import PyMongo
from .config import DevelopmentConfig

mongo = PyMongo()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    mongo.init_app(app)

    from .routes import users_bp
    app.register_blueprint(users_bp)

    return app
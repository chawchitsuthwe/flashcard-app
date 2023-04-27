__version__ = '0.1.0'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config_by_name
import os

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    return app

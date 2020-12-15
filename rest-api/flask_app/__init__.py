from flask import Flask
from flask_socketio import SocketIO

# Configuration and manage
from flask_app.commands import create_db, drop_db, populate_db, recreate_db
from flask_app.config import config

# Extensions
from flask_app.celery_worker import celery_worker
from flask_app.database import db
from flask_app.auth import jwt

# Blueprints
from flask_app.api import api
from flask_app.auth import auth
from flask_app.users import users
from flask_app.long_task import async_task


socketio = SocketIO(message_queue=config.REDIS_URI) if config.REDIS_URI else None


def create_app(*args):

    app = Flask(__name__)
    app.config.from_object(config)

    register_blueprints(app)
    register_extensions(app)
    register_commands(app)

    # # # TODO ERASE ! ! !
    app.app_context().push()    # # # TODO ERASE ! ! !
    recreate_db()               # # # TODO ERASE ! ! !
    # # # TODO ERASE ! ! !

    return app


def register_blueprints(app):
    app.register_blueprint(api)
    app.register_blueprint(auth)
    app.register_blueprint(users)
    app.register_blueprint(async_task)


def register_extensions(app):
    db.init_app(app)
    jwt.init_app(app)


def register_commands(app):
    for command in [create_db, drop_db, populate_db, recreate_db]:
        app.cli.command()(command)
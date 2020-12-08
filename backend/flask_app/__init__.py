from flask import Flask

# Configuration and manage
from flask_app.commands import create_db, drop_db, populate_db, recreate_db
from flask_app.config import config

# Extensions
from flask_app.celery_worker import celery_worker
from flask_app.websocket import socketio
from flask_app.database import db

# Blueprints
from flask_app.API import API


def create_app(*args):

    app = Flask(__name__)
    app.config.from_object(config)

    register_blueprints(app)
    register_extensions(app)
    register_commands(app)

    return app


def register_blueprints(app):
    app.register_blueprint(API)


def register_extensions(app):
    db.init_app(app)
    socketio.init_app(app, async_mode='eventlet', message_queue=config.REDIS_URI)


def register_commands(app):
    for command in [create_db, drop_db, populate_db, recreate_db]:
        app.cli.command()(command)
from flask import Flask

# Configuration
from flask_app.config import config

# Extensions
from flask_app.websocket import socketio


def create_app():

    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)

    return app


def register_extensions(app):
    socketio.init_app(app, async_mode='eventlet', message_queue=config.REDIS_URI)
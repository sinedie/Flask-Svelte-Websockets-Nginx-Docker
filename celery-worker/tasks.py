import os
import time

from celery import Celery
from celery.utils.log import get_task_logger
from flask_socketio import SocketIO


# Enviroment
ENV = os.environ.get("ENV")

# Redis
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']
REDIS_DB = os.environ['REDIS_DB']

# REDIS_URI = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
REDIS_URI = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'


class Config:
    ENV = ENV
    DEBUG = False
    TESTING = False
    REDIS_URI = REDIS_URI


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


class ProdConfig(Config):
    pass


if ENV == 'production':
    config = ProdConfig()
elif ENV == 'testing':
    config = TestConfig()
else:
    config = DevConfig()


app = Celery('tasks', broker=config.REDIS_URI, backend=config.REDIS_URI)
socketio = SocketIO(message_queue=config.REDIS_URI)
logger = get_task_logger(__name__)


@app.task()
def longtime_add(x, y):
    logger.info('Got Request - Starting work ')
    time.sleep(10)
    logger.info('Work Finished ')

    result = x + y

    socketio.emit('task_finished', {'result': result})
    return result

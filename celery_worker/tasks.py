import os
import time

from celery import Celery
from celery.utils.log import get_task_logger
from flask_socketio import SocketIO, emit

logger = get_task_logger(__name__)

REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']
REDIS_DB = os.environ['REDIS_DB']

# REDIS_URI = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
REDIS_URI = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'

app = Celery('tasks', broker=REDIS_URI, backend=REDIS_URI)
socketio = SocketIO(message_queue=REDIS_URI)


@app.task()
def longtime_add(x, y):
    logger.info('Got Request - Starting work ')
    time.sleep(10)
    logger.info('Work Finished ')

    print('sup')
    result = x + y

    socketio.emit('task_finished', {'result': result})
    return result

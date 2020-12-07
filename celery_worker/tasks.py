import time
from celery import Celery
from celery.utils.log import get_task_logger
from flask_socketio import SocketIO, emit

logger = get_task_logger(__name__)

app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')
socketio = SocketIO(message_queue='redis://redis:6379/0')


@app.task()
def longtime_add(x, y):
    logger.info('Got Request - Starting work ')
    time.sleep(10)
    logger.info('Work Finished ')

    result = x + y

    socketio.emit('task_finished', {'result': result})
    return result

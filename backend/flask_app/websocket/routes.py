from flask_socketio import emit

from flask_app.celery_worker import celery_worker
from flask_app.websocket.socket import socketio


@socketio.on("say_hi")
def on_my_event():
    print('sup')
    emit('greetings', {'message': 'Hey from websockets'})


@socketio.on('simple_start_task')
def call_method():
    r = celery_worker.send_task('tasks.longtime_add', kwargs={'x': 1, 'y': 2})
    return r.id
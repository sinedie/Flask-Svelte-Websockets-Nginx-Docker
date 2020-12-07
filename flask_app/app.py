from flask import Flask
from celery import Celery
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy


import config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

socketio = SocketIO(message_queue='redis://redis:6379/0')
socketio.init_app(app)

celery_worker = Celery('celery_worker', broker='redis://redis:6379/0', backend='redis://redis:6379/0')


@app.route('/api/say_hi')
def say_hey():
    return {'message': 'Hey from normal request'}


@socketio.on("say_hi")
def on_my_event():
    emit('greetings', {'message': 'Hey from websockets'})


@socketio.on('simple_start_task')
def call_method():
    app.logger.info("Invoking Method ")
    r = celery_worker.send_task('tasks.longtime_add', kwargs={'x': 1, 'y': 2})
    app.logger.info(r.backend)
    return r.id


if __name__ == '__main__':
    socketio.run(app)
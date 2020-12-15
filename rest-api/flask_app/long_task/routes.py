from flask import Blueprint, jsonify
from flask_jwt_extended import fresh_jwt_required

from flask_app.celery_worker import celery_worker


async_task = Blueprint('async_task', __name__, url_prefix="/api/async_task")


@async_task.route('/', methods=['GET'])
@fresh_jwt_required
def long_task():
    r = celery_worker.send_task('tasks.longtime_add', kwargs={'x': 1, 'y': 2})
    return jsonify({'msg': f'Running long task with id: {r.id}'}), 200
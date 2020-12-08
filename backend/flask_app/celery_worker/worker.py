from celery import Celery

from flask_app.config import config

celery_worker = Celery('celery_worker', broker=config.REDIS_URI, backend=config.REDIS_URI)
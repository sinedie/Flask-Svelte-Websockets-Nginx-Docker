FROM python:3.8-slim

COPY requirements.txt /
RUN pip install -r /requirements.txt

ADD . /flask_app
WORKDIR /flask_app

EXPOSE 5000

CMD gunicorn 'flask_app:create_app()' --worker-class eventlet -w 1 --bind 0.0.0.0:5000 --reload

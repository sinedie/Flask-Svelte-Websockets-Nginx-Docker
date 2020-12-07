FROM python:3.8-slim

# layer caching for faster builds
COPY requirements.txt /
RUN pip install -r /requirements.txt

ADD . /flask_app
WORKDIR /flask_app

ENV FLASK_ENV=development

EXPOSE 5000

#CMD python app.py
#CMD flask run --host=0.0.0.0

CMD gunicorn app:app --worker-class eventlet -w 1 --bind 0.0.0.0:5000 --reload

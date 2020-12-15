import uuid

from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash

from flask_app.database import db


class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)


    def __init__(self, username, email, password):
        self.username   = username
        self.email      = email
        self.password   = generate_password_hash(password)


    def __repr__(self):
        return '<User %r>' % self.username
        

    def verify_password(self, password):
        return check_password_hash(self.password, password)
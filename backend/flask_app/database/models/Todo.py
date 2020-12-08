from datetime import datetime

from flask_app.database import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(15), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    finished = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    # Example of relationships one to many
    ## To parent
    # owner = db.Column(db.Integer, db.ForeignKey("user.id"))
    ## To child
    # todo_sub_group = db.relationship("sub_todo", backref="todo")

    def __repr__(self):
        return f'<{self.title} finished: {self.finished}>'
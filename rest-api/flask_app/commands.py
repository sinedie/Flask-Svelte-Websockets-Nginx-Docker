import click

from flask_app.database import db, User


def populate_db():
    new_user = User('test', 'test@test.com', 'test')
    db.session.add(new_user)

    db.session.commit()


def create_db():
    db.create_all()


def drop_db():
    # if click.confirm('Are you sure?', abort=True):
    #     db.drop_all()
    db.drop_all()


def recreate_db():
    drop_db()
    create_db()
    populate_db()
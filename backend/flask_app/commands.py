import click

from flask_app.database import db, Todo


def populate_db():
    todos = [
        {
            "title": "todo_1",
            "description": "TODO 1",
        },
        {
            "title": "todo_2",
            "description": "TODO 2",
        },
        {
            "title": "todo_3",
            "description": "TODO 3",
        },
    ]


    for todo in todos:
        newTodo = Todo(
            title=todo["title"],
            description=todo["description"],
        )

        db.session.add(newTodo)
        # User.todos.append(newTodo) used to add a relationship

    db.session.commit()


def create_db():
    db.create_all()


def drop_db():
    if click.confirm('Are you sure?', abort=True):
        db.drop_all()


def recreate_db():
    drop_db()
    create_db()
    populate_db()
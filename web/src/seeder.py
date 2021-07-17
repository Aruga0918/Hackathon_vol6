import click
from flask.cli import with_appcontext
from models import User, Template
from database import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


@click.command("seed")
@click.argument("arg")
@with_appcontext
def seed(arg):
    if arg == "all":
        seed_user()
        seed_template()

    if arg == "user":
        seed_user()
    if arg == "template":
        seed_template()


def commit_all(objects):
    try:
        db.session.add_all(objects)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()


def seed_user():

    users = [
        User(
            uuid=f"uid{i}",
            name=f"sample{i}",
            password=bcrypt.generate_password_hash(f"password{i}").decode('utf-8')
        )
        for i in range(10)
    ]
    commit_all(users)


def seed_template():
    template = [
        Template(
            user_id=i % 10 + 1,
            description=f"{i}"
        )
        for i in range(20)
    ]
    commit_all(template)


def register_command(app):
    app.cli.add_command(seed)

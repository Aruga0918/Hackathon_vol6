
from database import db
from sqlalchemy.dialects.mysql import INTEGER


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    uuid = db.Column(db.String(28), nullable=False)
    name = db.Column(db.String(255), nullable=False)

    password = db.Column(db.String(60), nullable=False)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp(),
        server_onupdate=db.func.current_timestamp(),
        nullable=False,
    )
    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp(),
        server_onupdate=db.func.current_timestamp(),
        nullable=False,
    )

    def __init__(self, uuid, name, password):
        self.uuid = uuid
        self.name = name
        self.password = password

    def to_dict(self):
        return dict(
            name=self.name,
        )

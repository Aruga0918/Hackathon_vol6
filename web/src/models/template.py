from database import db
from sqlalchemy.dialects.mysql import INTEGER


class Template(db.Model):
    __tablename__ = "template"
    id = db.Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    user_id = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("users.id", ondelete="cascade", onupdate="cascade"),
        nullable=False,
    )

    description = db.Column(db.String(5000))

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

    def __init__(self, user_id, description=None):
        self.user_id = user_id
        self.description = description

    def to_dict(self):
        return dict(
            id=self.id,
            description="" if self.description is None else self.description,
            user_id=self.user_id,
            created_at=self.created_at,
        )

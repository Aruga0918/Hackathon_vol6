from database import db
from sqlalchemy.dialects.mysql import INTEGER


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(db.String(32), nullable=False)

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

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            created_at=self.created_at,
        )

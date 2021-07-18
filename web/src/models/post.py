from database import db
from sqlalchemy.dialects.mysql import INTEGER


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    user_id = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("users.id"),
        nullable=False,
    )

    shop_id = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("shops.id"),
        nullable=False,
    )

    message = db.Column(db.String(255))

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

    def __init__(self, user_id, shop_id, message=None):
        self.user_id = user_id
        self.shop_id = shop_id
        self.message = message

    def to_dict(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            shop_id=self.shop_id,
            message="" if self.message is None else self.message,
            created_at=self.created_at,
        )

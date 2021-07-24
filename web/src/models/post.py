from database import db
from sqlalchemy.dialects.mysql import INTEGER
from models.post_menu import PostMenu


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

    message = db.Column(db.String(255), default=None)

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

    menus = db.relationship(
        'Menu',
        secondary=PostMenu.__tablename__,
        back_populates='posts',
    )

    def to_dict(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            shop_id=self.shop_id,
            message="" if self.message is None else self.message,
            created_at=self.created_at,
        )

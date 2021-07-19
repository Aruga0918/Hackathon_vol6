from database import db
from sqlalchemy.dialects.mysql import INTEGER


class PostMenu(db.Model):
    __tablename__ = "posts_menus"

    post_id = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("posts.id"),
        nullable=False,
        primary_key=True
    )

    menu_id = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("menus.id"),
        nullable=False,
        primary_key=True
    )

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

    post = db.relationship('Post')
    menu = db.relationship('Menu')

    def __init__(self, post_id, menu_id):
        self.post_id = post_id
        self.menu_id = menu_id

    def to_dict(self):
        return dict(
            id=self.id,
            post_id=self.post_id,
            menu_id=self.menu_id,
            created_at=self.created_at,
        )

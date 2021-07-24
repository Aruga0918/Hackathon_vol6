from database import db
from sqlalchemy.dialects.mysql import INTEGER
from models.post_menu import PostMenu


class Menu(db.Model):
    __tablename__ = "menus"
    id = db.Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    shop_id = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("shops.id"),
        nullable=False,
    )

    name = db.Column(db.String(255), nullable=False)

    price = db.Column(INTEGER(unsigned=True), nullable=False)

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

    posts = db.relationship(
        'Post',
        secondary=PostMenu.__tablename__,
        back_populates=__tablename__,
    )

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            price=self.price,
            created_at=self.created_at,
        )

from database import db
from sqlalchemy.dialects.mysql import INTEGER


class Shop_Category(db.Model):
    __tablename__ = "shop_category"
    id = db.Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    shop_id = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("shop.id"),
        nullable=False,
    )

    category_id = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("category.id"),
        nullable=False,
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

    def __init__(self, shop_id, category_id):
        self.shop_id = shop_id
        self.category_id = category_id

    def to_dict(self):
        return dict(
            id=self.id,
            shop_id=self.shop_id,
            category_id=self.category_id,
            created_at=self.created_at,
        )

from database import db
from sqlalchemy.dialects.mysql import INTEGER, DOUBLE
from models.shop_category import ShopCategory


class Shop(db.Model):
    __tablename__ = "shops"
    id = db.Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(db.String(255), nullable=False)

    lattitude = db.Column(DOUBLE(9, 6),  default=None)
    longitude = db.Column(DOUBLE(9, 6), default=None)

    description = db.Column(db.String(255),  default=None)

    address = db.Column(db.String(255),  default=None)

    icon_url = db.Column(db.String(255),  default=None)

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

    categories = db.relationship(
        'Category',
        secondary=ShopCategory.__tablename__,
        back_populates='shops',
    )

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            lattitude="" if self.lattitude is None else self.lattitude,
            longitude="" if self.longitude is None else self.longitude,
            description="" if self.description is None else self.description,
            address="" if self.address is None else self.address,
            icon_url=self.icon_url,
            created_at=self.created_at,
        )

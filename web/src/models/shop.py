from database import db
from sqlalchemy.dialects.mysql import INTEGER, DOUBLE


class Shop(db.Model):
    __tablename__ = "shops"
    id = db.Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(db.String(32), nullable=False)

    lattitude = db.Column(DOUBLE(9, 6))
    longitude = db.Column(DOUBLE(9, 6))

    description = db.Column(db.String(255))

    address = db.Column(db.String(255))

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

    def __init__(self, name, lattitude=None, longitude=None, description=None, address=None):
        self.name = name
        self.lattitude = lattitude
        self.longitude = longitude
        self.description = description
        self.address = address

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            lattitude="" if self.lattitude is None else self.lattitude,
            longitude="" if self.longitude is None else self.longitude,
            description="" if self.description is None else self.description,
            address="" if self.address is None else self.address,
            created_at=self.created_at,
        )

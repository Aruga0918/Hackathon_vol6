from database import db
from sqlalchemy.dialects.mysql import INTEGER
from models.community_user import CommunityUser


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    uid = db.Column(db.String(32), nullable=False)
    name = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    icon_url = db.Column(db.String(255))
    profile = db.Column(db.String(255))

    is_private = db.Column(db.Boolean(), nullable=False)

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

    communities = db.relationship(
        'Community',
        secondary=CommunityUser.__tablename__,
        back_populates='users',
    )
    community_user = db.relationship('CommunityUser')

    def __init__(self, uid, name, password, icon_url=None, profile=None, is_private=False):
        self.uid = uid
        self.name = name
        self.password = password
        self.icon_url = icon_url
        self.profile = profile
        self.is_private = is_private

    def to_dict(self):
        return dict(
            uid=self.uid,
            name=self.name,
            icon_url="" if self.icon_url is None else self.icon_url,
            profile="" if self.profile is None else self.profile,
            is_private=self.is_private
        )

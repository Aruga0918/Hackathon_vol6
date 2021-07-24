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

    uid = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    icon_url = db.Column(db.String(255), default=None)
    profile = db.Column(db.String(255), default=None)

    is_private = db.Column(db.Boolean(), default=False)

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

    def to_dict(self):
        return dict(
            uid=self.uid,
            name=self.name,
            icon_url=self.icon_url,
            profile="" if self.profile is None else self.profile,
            is_private=self.is_private
        )

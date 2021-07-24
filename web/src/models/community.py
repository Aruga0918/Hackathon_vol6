from database import db
from sqlalchemy.dialects.mysql import INTEGER
from models.community_user import CommunityUser


class Community(db.Model):
    __tablename__ = "communities"
    id = db.Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(
        db.String(32),
        nullable=False,
    )

    icon_url = db.Column(db.String(255), default=None)

    description = db.Column(db.String(255), default=None)

    host_user = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("users.id"),
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

    users = db.relationship(
        'User',
        secondary=CommunityUser.__tablename__,
        back_populates='communities',
    )

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description="" if self.description is None else self.description,
            icon_url=self.icon_url,
            host_user=self.host_user,
            created_at=self.created_at,
        )

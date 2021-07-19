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

    comm_icon_url = db.Column(db.String(255))

    description = db.Column(db.String(255))

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
    community_user = db.relationship('CommunityUser')

    def __init__(self, name, host_user, comm_icon_url=None, description=None):
        self.name = name
        self.host_user = host_user
        self.comm_icon_url = comm_icon_url
        self.description = description

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description="" if self.description is None else self.description,
            comm_icon_url="" if self.comm_icon_url is None else
            self.comm_icon_url,
            host_user=self.host_user,
            created_at=self.created_at,
        )

from database import db
from sqlalchemy.dialects.mysql import INTEGER


class CommunityUser(db.Model):
    __tablename__ = "communities_users"

    id = db.Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    community_id = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("communities.id"),
        nullable=False,
    )

    user_id = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("users.id"),
        nullable=False,
    )

    is_join = db.Column(db.Boolean(), nullable=False)

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

    def to_dict(self):
        return dict(
            id=self.id,
            community_id=self.community_id,
            user_id=self.user_id,
            is_join=self.is_join,
            created_at=self.created_at,
        )

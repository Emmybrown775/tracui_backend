import uuid

from sqlalchemy.dialects.postgresql import UUID
from app.extensions import db
import datetime




class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    access_token = db.Column(db.String(), nullable=False)
    access_secret = db.Column(db.String(), nullable=True)
    email = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False,  default=datetime.datetime.now())
    account_type = db.Column(db.String(), nullable=False)


    def as_dict(self):
        return {
            c.name: str(getattr(self, c.name)) if isinstance(getattr(self, c.name), uuid.UUID) else getattr(self,
                                                                                                            c.name)
            for c in self.__table__.columns
            if c.name != "password"
        }




















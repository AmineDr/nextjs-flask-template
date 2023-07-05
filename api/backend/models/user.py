import uuid
from backend.models import db
from datetime import datetime
from werkzeug.security import check_password_hash


class User(db.Model):
    __tablename__ = 'user'

    ID = db.Column(db.String(64), primary_key=True, default=lambda x: uuid.uuid4().__str__())

    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(256))

    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User : {self.username} #{self.ID}"

    def check_login(self, password):
        if check_password_hash(self.password, password):
            return True
        return False

    def to_dict(self):
        return {
            "id": self.ID,
            "username": self.username,
            "last_login": self.last_login,
            "date_created": self.date_created
        }

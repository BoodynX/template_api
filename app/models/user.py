from datetime import datetime

from sqlalchemy import DateTime

from app.framework.database import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    created_at = db.Column(DateTime, default=datetime.utcnow)

    def __init__(self, username: str = None, password: str = None):
        self.username = username
        self.password = password

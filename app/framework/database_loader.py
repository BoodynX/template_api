from flask import Flask
from app.framework.database import db


class DatabaseLoader:
    """This is separate from the database.py because it is being used after flask is being instantiated"""

    @classmethod
    def load(cls, flask: Flask):
        @flask.before_first_request
        # Create tables if they don't exist
        def create_tables():
            db.create_all()

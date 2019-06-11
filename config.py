import os

DEBUG = os.environ.get("DEBUG")
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///default.db")

# This setting turns off the Flask-SQLAlchemy changes tracker,
# because the basic SQLAlchemy tracker works better (more efficiently)
SQLALCHEMY_TRACK_MODIFICATIONS = False

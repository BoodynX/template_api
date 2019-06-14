import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from marshmallow import ValidationError

from app.framework.database import db
from app.framework.translations import load_translation
from app.routes import load_routes

# setting up consistent working directory in case test are run
os.chdir(os.path.dirname(os.path.realpath(__file__)))
load_dotenv(".env", verbose=True)

flask = Flask(__name__)
flask.config.from_pyfile('config.py')


@flask.before_first_request
# Create tables if they don't exist
def create_tables():
    db.create_all()


@flask.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


load_translation(os.environ.get("DEFAULT_LOCALE", "en-us"))
load_routes(flask)

if __name__ == '__main__':
    db.init_app(flask)
    flask.run(port=5000)

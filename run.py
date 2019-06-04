import os

from dotenv import load_dotenv
from flask import Flask

from app.framework.db import db
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


load_translation(os.environ.get("DEFAULT_LOCALE", "en-us"))
load_routes(flask)

if __name__ == '__main__':
    db.init_app(flask)

    # if flask.debug:
    #     @flask.before_first_request
    #     # Create tables if they don't exist
    #     def create_tables():
    #         db.create_all()

    flask.run(port=5000)

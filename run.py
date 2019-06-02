import os

from dotenv import load_dotenv
from flask import Flask

from app.bootstrap.db import db
from app.libs.translations import load_translation
from app.routes import routes

# setting up consistent working directory in case test are run
os.chdir(os.path.dirname(os.path.realpath(__file__)))
load_dotenv(".env", verbose=True)
load_translation(os.environ.get("DEFAULT_LOCALE", "en-us"))

flask = Flask(__name__)
flask.debug = os.environ.get("DEBUG")

routes(flask)

if __name__ == '__main__':
    db.init_app(flask)
    flask.run(port=5000)

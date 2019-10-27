import os

from dotenv import load_dotenv
from flask import Flask

from app.framework.database import db
from app.framework.database_loader import DatabaseLoader
from app.framework.error_handlers import ErrorHandlers
from app.framework.translations import load_translation
from app.routes import Routes

# setting up consistent working directory in case test are run
os.chdir(os.path.dirname(os.path.realpath(__file__)))
load_dotenv(".env", verbose=True)

flask = Flask(__name__)
flask.config.from_pyfile('config.py')

# Load framework components
load_translation(os.environ.get("DEFAULT_LOCALE", "en-us"))
DatabaseLoader.load(flask)
ErrorHandlers.load(flask)
Routes.load(flask)

if __name__ == '__main__':
    db.init_app(flask)
    flask.run(port=5000)

import os

from flask import Flask
from flask_restful import Api

from app.libs.translations import refresh
from app.resources.home import Home
from app.resources.user.registration import Registration

# setting up consistent working directory in case test are run
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# load translations
refresh()

app = Flask(__name__)
app.config['DEBUG'] = True
api = Api(app)

api.add_resource(Home, '/')
api.add_resource(Registration, '/registration')

if __name__ == '__main__':
    app.run(port=5000)

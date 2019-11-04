from flask import Flask
from flask_restful import Api

from app.resources.home import Home
from app.resources.user import UsersResource
from tests.framework.routes import load_test_routes


class Routes:
    HOME = '/'
    USER_REGISTRATION = '/user'

    @classmethod
    def load(cls, flask: Flask):
        api = Api(flask)

        api.add_resource(Home, cls.HOME)
        api.add_resource(UsersResource, cls.USER_REGISTRATION)

        if flask.config['ENV'] == 'development':
            # this is set as FLASK_ENV in the .env
            cls.load_test_routes(flask)

    @classmethod
    def load_test_routes(cls, flask):
        load_test_routes(flask)

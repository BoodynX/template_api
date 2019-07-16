from flask import Flask
from flask_restful import Api

from app.resources.home import Home
from app.resources.user import UserRegistration


class Routes:
    HOME = '/'
    USER_REGISTRATION = '/user/registration'

    @classmethod
    def load(cls, flask: Flask):
        api = Api(flask)

        api.add_resource(Home, cls.HOME)
        api.add_resource(UserRegistration, cls.USER_REGISTRATION)


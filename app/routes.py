from flask import Flask
from flask_restful import Api

from app.resources.home import Home
from app.resources.user.registration import Registration


def load_routes(flask: Flask):
    api = Api(flask)

    api.add_resource(Home, '/')
    api.add_resource(Registration, '/registration')


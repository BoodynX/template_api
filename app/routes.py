from flask import Flask
from flask_restful import Api

from app.resources.home import Home
from app.resources.user.registration import Registration


def routes(app: Flask):
    api = Api(app)

    api.add_resource(Home, '/')
    api.add_resource(Registration, '/registration')


from flask_restful import Resource

from app.libs.translations import gettext


class Home(Resource):
    def get(self):
        return {'message': gettext('hello_template')}, 200

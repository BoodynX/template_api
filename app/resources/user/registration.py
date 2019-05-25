from flask_restful import Resource


class Registration(Resource):

    def post(self):
        return {}, 201

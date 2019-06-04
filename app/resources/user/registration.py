from flask_restful import Resource

from app.models.user import UserModel


class Registration(Resource):

    def post(self):
        user_model = UserModel
        user_model.username = 'dummy'
        user_model.save_to_db()

        return {}, 201

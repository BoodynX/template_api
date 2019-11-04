from flask import request
from flask_restful import Resource

from app.repositories.user import UserRepository
from app.schemas.user_registration_schema import UserRegistrationSchema


class UsersResource(Resource):

    def post(self):
        user = UserRegistrationSchema.handle_request(request.get_json())
        UserRepository.create(user)

        return {}, 201

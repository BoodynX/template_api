from marshmallow import fields, post_load

from app.entities.user import User
from app.schemas.validator import Validator


class UserRegistrationSchema(Validator):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

    @post_load
    def make_user_entity(self, data) -> User:
        return User(username=data['username'], password=data['password'])

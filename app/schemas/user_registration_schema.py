from marshmallow import fields, post_load, validate

from app.entities.user import User
from app_config import PASSWORD_MIN_LENGTH, USERNAME_MIN_LENGTH
from app.schemas.base_schema import BaseSchema
from app.schemas.validators.is_alphanumeric import IsAlphanumeric


class UserRegistrationSchema(BaseSchema):
    username = fields.Str(required=True,
                          validate=[IsAlphanumeric(), validate.Length(min=USERNAME_MIN_LENGTH)])
    password = fields.Str(required=True, validate=validate.Length(min=PASSWORD_MIN_LENGTH))

    @post_load
    def make_user_entity(self, data: dict) -> User:
        return User(username=data['username'], password=data['password'])

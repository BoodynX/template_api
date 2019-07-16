from marshmallow import fields, post_load

from app.entities.user import User
from app.schemas.base_schema import BaseSchema
from app.schemas.validators.is_alphanumeric import IsAlphanumeric
from app.schemas.validators.not_empty_str import NotEmptyStr


class UserRegistrationSchema(BaseSchema):
    username = fields.Str(required=True, validate=IsAlphanumeric())
    password = fields.Str(required=True, validate=NotEmptyStr())

    @post_load
    def make_user_entity(self, data: dict) -> User:
        return User(username=data['username'], password=data['password'])

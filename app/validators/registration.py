from marshmallow import fields, post_load

from app.requests.registration import Registration
from app.validators.validator import Validator


class RegistrationValidator(Validator):
    username = fields.Str()
    password = fields.Str()

    @post_load
    def make_registration_request(self, data) -> Registration:
        return Registration(username=data['username'], password=data['password'])

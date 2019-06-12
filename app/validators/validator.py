from marshmallow import Schema


class Validator(Schema):
    @classmethod
    def handle_request(cls, json):
        validator = cls()
        return validator.load(json)

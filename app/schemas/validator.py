from marshmallow import Schema


class Validator(Schema):
    @classmethod
    def handle_request(cls, json: dict):
        validator = cls()
        return validator.load(json)

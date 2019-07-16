from marshmallow import Schema


class BaseSchema(Schema):
    @classmethod
    def handle_request(cls, json: dict):
        schema = cls()
        return schema.load(json)

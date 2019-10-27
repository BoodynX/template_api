from flask import Flask, jsonify
from marshmallow import ValidationError


class ErrorHandlers:
    @classmethod
    def load(cls, flask: Flask):
        @flask.errorhandler(ValidationError)
        def handle_marshmallow_validation(err):
            return jsonify(err.messages), 400

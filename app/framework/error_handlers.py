from json import JSONDecodeError
from flask import Flask, jsonify
from marshmallow import ValidationError
from sqlalchemy import exc
from werkzeug.exceptions import InternalServerError

from app.framework.http_responses import response


class ErrorHandlers:
    RESPONSE_BODY_400 = {
        "error": "bad_request",
        "error_description": "Bad Request"
    }
    RESPONSE_BODY_401 = {
        'error': 'unauthorized',
        'error_description': 'Unauthorized'
    }
    RESPONSE_BODY_405 = {
        "error": "invalid_method",
        "error_description": "Method is not allowed"
    }

    # Error codes for internal server errors on production
    ERROR_CODE_GENERIC_500 = '1'
    ERROR_CODE_DB_TIMEOUT = '2'
    ERROR_CODE_JSON_DECODE = '3'

    ERROR_KEY_INVALID_PARAMETERS = 'invalid_parameters'

    @classmethod
    def load(cls, flask: Flask):
        @flask.errorhandler(ValidationError)
        def handle_marshmallow_validation(err):
            return jsonify(err.messages), 400

        @flask.errorhandler(400)
        def bad_request(error: InternalServerError):
            return response(cls.RESPONSE_BODY_400, 400)

        @flask.errorhandler(401)
        def unauthorized(error: InternalServerError):
            return response(cls.RESPONSE_BODY_401, 401)

        @flask.errorhandler(404)
        def not_found(error: InternalServerError):
            return response({}, 404)

        @flask.errorhandler(405)
        def invalid_method(error: InternalServerError):
            return response(cls.RESPONSE_BODY_405, 405)

        @flask.errorhandler(500)
        def handle_internal_error(error: InternalServerError):
            return response(cls._internal_server_error_response(cls.ERROR_CODE_GENERIC_500), 500)

        @flask.errorhandler(ValidationError)
        def handle_marshmallow_validation(error):
            return jsonify({'error': cls.ERROR_KEY_INVALID_PARAMETERS, 'parameters': error.messages}), 400

        # This is for catching database connection fails
        @flask.errorhandler(exc.OperationalError)
        def handle_sqlalchemy_operational_error(error):
            return response(cls._internal_server_error_response(cls.ERROR_CODE_DB_TIMEOUT), 500)

        @flask.errorhandler(JSONDecodeError)
        def handle_sqlalchemy_operational_error(error):
            return response(cls._internal_server_error_response(cls.ERROR_CODE_JSON_DECODE), 500)

    @classmethod
    def _internal_server_error_response(cls, code: str):
        return {
            'error': 'server_error',
            'error_description': f'error code {code}'
        }

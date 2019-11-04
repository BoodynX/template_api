from flask import make_response, jsonify


def response(body: dict, code: int = 200):
    return make_response(jsonify(body), code)

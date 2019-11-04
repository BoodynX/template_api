from flask import Flask, abort

# from app.resources.api_client import ApiClientResource
from app.framework.http_responses import response

PING_URL = '/ping'
PING_400_URL = '/ping_400'
PING_401_URL = '/ping_401'
PING_404_URL = '/ping_404'
PING_405_URL = '/ping_405'
PING_500_URL = '/ping_500'
AUTH_PING_URL = '/auth_ping'
API_CLIENT_URL = '/admin/api_client'


def load_test_routes(flask: Flask):
    @flask.route(PING_URL)
    def ping():
        return response({'message': 'Pong!'})

    # @flask.route(AUTH_PING_URL)
    # @jwt_required
    # def auth_ping():
    #     return response({'message': 'Auth Pong!'})
    #
    # @flask.route(API_CLIENT_URL, methods=['POST'])
    # @jwt_required
    # def create_api_client():
    #     return ApiClientResource.create()

    @flask.route(PING_400_URL)
    def ping_400():
        abort(400)

    @flask.route(PING_401_URL)
    def ping_401():
        abort(401)

    @flask.route(PING_404_URL)
    def ping_404():
        abort(404)

    @flask.route(PING_405_URL)
    def ping_405():
        abort(405)

    @flask.route(PING_500_URL)
    def ping_500():
        abort(500)

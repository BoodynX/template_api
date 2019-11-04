import json

from app.framework.error_handlers import ErrorHandlers
from app.framework.globals import MIMETYPE_JSON
from tests.framework.routes import PING_400_URL, PING_401_URL, PING_500_URL, PING_404_URL, PING_405_URL
from tests.framework.tests_base_classes.app_test import AppTest


class TestErrorHandlers(AppTest):
    def test_400(self):
        with self.app_client() as client:
            response = client.get(PING_400_URL)

            self.assertEqual(MIMETYPE_JSON, response.mimetype)
            self.assertEqual(400, response.status_code)
            self.assertDictEqual(
                {
                    'error': 'bad_request',
                    'error_description': 'Bad Request'
                },
                json.loads(response.data)
            )

    def test_401(self):
        with self.app_client() as client:
            response = client.get(PING_401_URL)

            self.assertEqual(MIMETYPE_JSON, response.mimetype)
            self.assertEqual(401, response.status_code)
            self.assertDictEqual(
                ErrorHandlers.RESPONSE_BODY_401,
                json.loads(response.data)
            )

    def test_404(self):
        with self.app_client() as client:
            response = client.get(PING_404_URL)

            self.assertEqual(MIMETYPE_JSON, response.mimetype)
            self.assertEqual(404, response.status_code)
            self.assertDictEqual(
                {},
                json.loads(response.data)
            )

    def test_405(self):
        with self.app_client() as client:
            response = client.get(PING_405_URL)

            self.assertEqual(MIMETYPE_JSON, response.mimetype)
            self.assertEqual(405, response.status_code)
            self.assertDictEqual(
                ErrorHandlers.RESPONSE_BODY_405,
                json.loads(response.data)
            )

    def test_500(self):
        with self.app_client() as client:
            response = client.get(PING_500_URL)
            response_json = response.get_json()

            self.assertEqual(MIMETYPE_JSON, response.mimetype)
            self.assertEqual(500, response.status_code)
            self.assertDictEqual(ErrorHandlers._internal_server_error_response(ErrorHandlers.ERROR_CODE_GENERIC_500),
                                 response_json)

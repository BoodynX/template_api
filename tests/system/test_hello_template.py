import json

from tests.app_test import AppTest


class TestHelloTemplate(AppTest):

    def test_home(self):
        with self.app_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertDictEqual(
                json.loads(response.data),
                {'message': 'Hello Template!'}
            )

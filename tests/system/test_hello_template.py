import json

from tests.system.base_system_test import BaseSystemTest


class TestHelloTemplate(BaseSystemTest):

    def test_home(self):
        with self.app_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertDictEqual(
                {'message': 'Hello Template!'},
                json.loads(response.data)
            )
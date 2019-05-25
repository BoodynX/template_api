from tests.system.base_system_test import BaseSystemTest


class TestRegistration(BaseSystemTest):

    def test_submit_for_an_account(self):
        with self.app_client() as client:
            response = client.post(
                '/registration',
                data={'login': 'John', 'password': 'Jack1'}
            )

            self.assertEqual(response.status_code, 201)

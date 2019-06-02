from tests.app_test import AppTest


class TestRegistration(AppTest):

    def test_submit_for_an_account(self):
        with self.app_client() as client:
            response = client.post(
                '/registration',
                data={'login': 'John', 'password': 'Jack1'}
            )

            self.assertEqual(response.status_code, 201)

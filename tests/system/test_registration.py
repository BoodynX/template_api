import json

from app.repositories.user import UserRepository
from app.routes import Routes
from app_config import PASSWORD_MIN_LENGTH, USERNAME_MIN_LENGTH
from tests.framework.tests_base_classes.app_test import AppTest

USER_NAME = 'TestRegistrationUserName'
PASSWORD = 'TestRegistrationPassword'


class TestRegistration(AppTest):

    def test_submit_for_an_account_with_correct_data(self):
        with self.app_client() as client:
            with self.app_context():
                response = self.register_user(client, USER_NAME, PASSWORD)
                user = UserRepository.find_by_username(USER_NAME)

                self.assertEqual(201, response.status_code)
                self.assertEqual(USER_NAME, user.username)
                self.assertEqual(PASSWORD, user.password)

    def test_submit_for_an_account_with_empty_user_name(self):
        with self.app_client() as client:
            with self.app_context():
                response = self.register_user(client, '', PASSWORD)
                self.assertEqual(400, response.status_code)
                self.assertDictEqual(
                    {
                        "error": "invalid_parameters",
                        "parameters": {
                            "username":  ['Invalid value.',
                                          f"Shorter than minimum length {USERNAME_MIN_LENGTH}."]
                        }
                    },
                    json.loads(response.data)
                )

    def test_submit_for_an_account_with_empty_password(self):
        with self.app_client() as client:
            with self.app_context():
                response = self.register_user(client, USER_NAME, '')
                self.assertEqual(400, response.status_code)
                self.assertDictEqual(
                    {
                        "error": "invalid_parameters",
                        "parameters": {
                            "password": [f"Shorter than minimum length {PASSWORD_MIN_LENGTH}."]
                        }
                    },
                    json.loads(response.data)
                )

    def test_submit_for_an_account_with_invalid_username(self):
        with self.app_client() as client:
            with self.app_context():
                response = self.register_user(client, 'Some strange characters -> $%^&*)_>+', PASSWORD)
                self.assertEqual(400, response.status_code)
                self.assertDictEqual(
                    {
                        "error": "invalid_parameters",
                        "parameters": {
                            "username": [
                                "Invalid value."
                            ]
                        }
                    },
                    json.loads(response.data)
                )

    def test_submit_for_an_account_with_missing_form_fields(self):
        with self.app_client() as client:
            with self.app_context():
                response = client.post(
                    Routes.USER_REGISTRATION,
                    data=json.dumps({}),
                    headers={'Content-Type': 'application/json'}
                )
                self.assertEqual(400, response.status_code)
                self.assertDictEqual(
                    {
                        "error": "invalid_parameters",
                        "parameters": {
                            "password": [
                                "Missing data for required field."
                            ],
                            "username": [
                                "Missing data for required field."
                            ]
                        }
                    },
                    json.loads(response.data)
                )

    def register_user(self, client, username, password):
        return client.post(
            Routes.USER_REGISTRATION,
            data=json.dumps({'username': username, 'password': password}),
            headers={'Content-Type': 'application/json'}
        )

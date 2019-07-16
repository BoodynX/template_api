import json

from app.repositories.user import UserRepository
from app.routes import Routes
from tests.app_test import AppTest

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

    def test_submit_for_an_account_with_empty_password(self):
        with self.app_client() as client:
            with self.app_context():
                response = self.register_user(client, USER_NAME, '')
                self.assertEqual(400, response.status_code)

    def test_submit_for_an_account_with_invalid_username(self):
        with self.app_client() as client:
            with self.app_context():
                response = self.register_user(client, 'Some strange characters -> $%^&*)_>+', PASSWORD)
                self.assertEqual(400, response.status_code)

    def register_user(self, client, username, password):
        return client.post(
            Routes.USER_REGISTRATION,
            data=json.dumps({'username': username, 'password': password}),
            headers={'Content-Type': 'application/json'}
        )

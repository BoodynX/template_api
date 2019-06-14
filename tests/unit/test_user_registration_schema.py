from app.entities.user import User
from app.schemas.user_registration_schema import UserRegistrationSchema
from tests.app_test import AppTest

USER_NAME = 'usernameTestUserRegistrationSchema'
PASSWORD = 'passwordTestUserRegistrationSchema'


class TestUserRegistrationSchema(AppTest):

    def test_registration_schema(self):
        registration_form = {'username': USER_NAME, 'password': PASSWORD}
        user_post_schema = UserRegistrationSchema()

        registration = user_post_schema.load(registration_form)

        self.assertIsInstance(registration, User)
        self.assertEqual(registration.username, USER_NAME)

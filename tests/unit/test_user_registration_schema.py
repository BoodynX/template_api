from app.entities.user import User
from app.schemas.user_registration_schema import UserRegistrationSchema
from tests.app_test import AppTest


class TestUserRegistrationSchema(AppTest):

    def test_registration_schema(self):
        registration_form = {'username': 'Test Username', 'password': 'Test Password'}
        user_post_schema = UserRegistrationSchema()

        registration = user_post_schema.load(registration_form)

        self.assertIsInstance(registration, User)
        self.assertEqual(registration.username, 'Test Username')

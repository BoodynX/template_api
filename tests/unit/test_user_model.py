from app.models.user import UserModel
from tests.framework.tests_base_classes.base_test import BaseTest

USER_NAME = 'username TestUserModel'
PASSWORD = 'password TestUserModel'


class TestUserModel(BaseTest):
    def test_create_user(self):
        user = UserModel(USER_NAME, PASSWORD)

        self.assertEqual(user.username, USER_NAME,
                         "The name of the user after creation does not equal the constructor argument.")
        self.assertEqual(user.password, PASSWORD,
                         "The password of the user after creation does not equal the constructor argument.")

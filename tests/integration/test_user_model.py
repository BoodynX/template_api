from app.models.user import UserModel
from tests.app_test import AppTest

USER_ID = 1
PASSWORD = 'Test Password'
USER_NAME = 'Test User'


class TestUserModel(AppTest):
    def test_save_and_read(self):
        with self.app_context():
            user_model_to_save = UserModel(USER_NAME, PASSWORD)
            user_model_to_save.save_to_db()

            user_by_id = UserModel.find_by_id(USER_ID)
            user_by_name = UserModel.find_by_username(USER_NAME)

            self.assertEqual(USER_ID, user_by_id.id)
            self.assertEqual(USER_NAME, user_by_name.username)

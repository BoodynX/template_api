from app.entities.user import User
from app.repositories.user import UserRepository
from tests.framework.tests_base_classes.app_test import AppTest

USER_ID = 1
PASSWORD = 'Test Password'
USER_NAME = 'Test UserRegistration'


class TestUserRepository(AppTest):
    def test_save_and_read(self):
        with self.app_context():
            user = User(username=USER_NAME, password=PASSWORD)
            UserRepository.create(user=user)

            user_by_id = UserRepository.find_by_id(USER_ID)
            user_by_name = UserRepository.find_by_username(USER_NAME)

            self.assertEqual(USER_ID, user_by_id.id_)
            self.assertEqual(USER_NAME, user_by_name.username)

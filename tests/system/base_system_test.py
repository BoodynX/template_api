from tests.base_test import BaseTest

from run import app


class BaseSystemTest(BaseTest):
    def setUp(self):
        self.app_client = app.test_client
        self.app_context = app.app_context

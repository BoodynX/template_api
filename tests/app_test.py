from tests.base_test import BaseTest

from run import flask


class AppTest(BaseTest):
    def setUp(self):
        self.app_client = flask.test_client
        self.app_context = flask.app_context

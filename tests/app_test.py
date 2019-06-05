from app.framework.db import db
from run import flask
from tests.base_test import BaseTest


class AppTest(BaseTest):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"

    @classmethod
    def setUpClass(cls):
        flask.config['SQLALCHEMY_DATABASE_URI'] = AppTest.SQLALCHEMY_DATABASE_URI
        flask.config['DEBUG'] = False
        with flask.app_context():
            db.init_app(flask)

    def setUp(self):
        with flask.app_context():
            db.create_all()
        self.app_client = flask.test_client
        self.app_context = flask.app_context

    def tearDown(self):
        with flask.app_context():
            db.session.remove()
            db.drop_all()

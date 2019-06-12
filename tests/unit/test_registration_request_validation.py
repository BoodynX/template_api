from app.requests.registration import Registration
from app.validators.registration import RegistrationValidator
from tests.app_test import AppTest


class TestRegistrationRequestValidation(AppTest):

    def test_registration_request(self):
        registration_form = {'username': 'Test Username', 'password': 'Test Password'}
        registration_schema = RegistrationValidator()

        registration = registration_schema.load(registration_form)

        self.assertIsInstance(registration, Registration)
        self.assertEqual(registration.username, 'Test Username')

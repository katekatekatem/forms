from django.test import TestCase

from forms_app.validators import (
    validate_date, validate_email, validate_phone,
)


class TestValidators(TestCase):

    def test_validate_date(self):
        self.assertTrue(validate_date('2022-01-01'))
        self.assertTrue(validate_date('01.01.2022'))
        self.assertFalse(validate_date('2022-01-32'))
        self.assertFalse(validate_date('01.13.2022'))
        self.assertFalse(validate_date('01/01/2022'))

    def test_validate_phone(self):
        self.assertTrue(validate_phone('+7 123 456 78 90'))
        self.assertFalse(validate_phone('+7 123 456 78'))
        self.assertFalse(validate_phone('1234567890'))
        self.assertFalse(validate_phone('123-456-7890'))

    def test_validate_email(self):
        self.assertTrue(validate_email('test@example.com'))
        self.assertFalse(validate_email('invalid_email'))
        self.assertFalse(validate_email('test@example'))

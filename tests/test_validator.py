import unittest

from validator import validate_contact


class TestContactValidation(unittest.TestCase):
    def test_valid_contact(self):
        self.assertTrue(validate_contact("Asha", "9876543210", "asha@example.com")[0])

    def test_blank_name(self):
        self.assertFalse(validate_contact(" ", "9876543210", "asha@example.com")[0])

    def test_phone_must_be_ten_digits(self):
        self.assertFalse(validate_contact("Asha", "98765", "asha@example.com")[0])

    def test_phone_must_start_with_valid_digit(self):
        self.assertFalse(validate_contact("Asha", "5123456789", "asha@example.com")[0])

    def test_email_must_have_one_at_symbol(self):
        self.assertFalse(validate_contact("Asha", "9876543210", "asha@@example.com")[0])

    def test_email_domain_needs_dot(self):
        self.assertFalse(validate_contact("Asha", "9876543210", "asha@example")[0])


if __name__ == "__main__":
    unittest.main()

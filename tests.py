import unittest
from password_manager import is_strong_password, generate_strong_password

class TestPasswordManager(unittest.TestCase):
    def test_is_strong_password_valid(self):
        # Test valid passwords
        valid_passwords = [
            "Abcd123!@#",
            "P@ssw0rd123",
            "Str0ng!Pass",
            "a" * 50 + "B1!",  # Long but valid password
        ]
        for password in valid_passwords:
            with self.subTest(password=password):
                self.assertTrue(is_strong_password(password))

    def test_is_strong_password_invalid(self):
        # Test invalid passwords
        invalid_passwords = [
            "",  # Empty password
            "short",  # Too short
            "a" * 101,  # Too long
            "abcd1234",  # No uppercase
            "ABCD1234",  # No lowercase
            "ABCDabcd",  # No numbers
            "ABCDabcd123",  # No special characters
            "Ab1!",  # Too short but has all character types
        ]
        for password in invalid_passwords:
            with self.subTest(password=password):
                self.assertFalse(is_strong_password(password))

    def test_generate_strong_password_custom_length(self):
        # Test password generation with custom lengths
        test_lengths = [8, 16, 32, 100]
        for length in test_lengths:
            with self.subTest(length=length):
                password = generate_strong_password(length)
                self.assertEqual(len(password), length)
                self.assertTrue(is_strong_password(password))

    def test_generate_strong_password_invalid_length(self):
        # Test password generation with invalid lengths
        invalid_lengths = [0, -1, 7, 101]
        for length in invalid_lengths:
            with self.subTest(length=length):
                with self.assertRaises(ValueError):
                    generate_strong_password(length)

    def test_generate_strong_password_uniqueness(self):
        # Test that generated passwords are unique
        passwords = [generate_strong_password(8) for _ in range(5)]
        unique_passwords = set(passwords)
        self.assertEqual(len(passwords), len(unique_passwords))

if __name__ == '__main__':
    unittest.main() 
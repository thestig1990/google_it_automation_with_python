#!/usr/bin/ python3


import unittest


from raising_errors import validate_user


class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validuser", 3), True)
        
    def test_to_short(self):
        self.assertEqual(validate_user("inv", 5), False)

    def test_invalid_character(self):
        self.assertEqual(validate_user("invalid_user", 1), False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user, "username", -1)



# Run test
if __name__ == "__main__":
    unittest.main()
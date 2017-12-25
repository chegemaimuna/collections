"""import objects"""
import unittest
from flaskapp.models import Account

class TestRecipeSignupAndLogin(unittest.TestCase):
    """test for successful and unsuccessful signup and login"""
    def setUp(self):
        self.acc = Account()
    # signup tests
    def test_signup_success(self):
        """returns True if signup was successful"""
        result = self.acc.adduser("name", "email", "password", "password")
        self.assertEqual(True, result)
    def test_signup_failure(self):
        """returns False if a signup process was unsuccessful"""
        result = self.acc.adduser("user", "email", "password", "password")
        self.assertNotEqual(False, result)
    def test_password_mismatch(self):
        """returns True for password mismatch"""
        result = self.acc.adduser("name", "email", "password", "mismatched")
        self.assertEqual("pass_fail", result)
    def test_user_existence(self):
        """returns false if a user exists"""
        self.acc.adduser("name", "email", "password", "password")
        result = self.acc.adduser("name", "email", "password", "password")
        self.assertEqual(False, result)
    # login tests
    def test_login_failure(self):
        """returns success if login is successful"""
        self.acc.adduser("name", "email", "password", "password")
        result = self.acc.login("name", "password")
        self.assertEqual(True, result)
    def test_login_success(self):
        """returns false if login is unsuccessful"""
        self.acc.adduser("name", "email", "password", "password")
        result = self.acc.login("name", "wrong_password")
        self.assertEqual(False, result)
if __name__ == '__main__':
    unittest.main()
    
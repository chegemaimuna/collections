"""import from libraries"""
# import the standard unittest
import unittest
# import account & list classes from models.py
from flaskapp.models import *

class TestRecipeSignupAndLogin(unittest.TestCase):
    """test for successful and unsuccessful signup and login"""
    def setUp(self):
        self.acc = Account()
        self.list = Lists()
    #"""
    #
    #signup tests
    #
    #"""
    def test_signup_success(self):
        """returns True if signup was successful"""
        result = self.acc.adduser("name", "username@domain.com", "1@Strongpass", "1@Strongpass")
        self.assertEqual(True, result)
    def test_signup_failure(self):
        """returns False if a signup process was unsuccessful"""
        result = self.acc.adduser("name", "username@domain.com", "1@Strongpass", "1@Strongpass")
        self.assertNotEqual(False, result)
    def test_password_mismatch(self):
        """returns pass_fail for password mismatch"""
        result = self.acc.adduser("name", "username@domain.com", "1@Strongpass", "1@Mismatchted")
        self.assertEqual("pass_fail", result)
    def test_user_existence(self):
        """returns false if a user exists"""
        self.acc.adduser("name", "username@domain.com", "1@Strongpass", "1@Strongpass")
        result = self.acc.adduser("name", "username@domain.com", "1@Strongpass", "1@Strongpass")
        self.assertEqual(False, result)
    #"""
    #
    #login tests
    #
    #"""
    def test_login_failure(self):
        """returns success if login is successful"""
        self.acc.adduser("name", "username@domain.com", "1@Strongpass", "1@Strongpass")
        result = self.acc.login("name", "1@Strongpass")
        self.assertEqual(True, result)
    def test_login_success(self):
        """returns false if login is unsuccessful"""
        self.acc.adduser("name", "username@domain.com", "1@Strongpass", "1@Strongpass")
        result = self.acc.login("name", "wrong_1@Strongpass")
        self.assertEqual(False, result)

    """
    #
    #List Tests
    #
    """
    def test_addrecipe(self):
        """returns true if a colletion title was added successfully"""
        result = self.list.addrecipe("name", "title")
        self.assertEqual(True, result)

if __name__ == '__main__':
    unittest.main()
    
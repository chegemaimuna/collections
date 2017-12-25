import unittest
from flaskapp.models import Account

class RecipeSignup(unittest.TestCase):
    def setUp(self):
        self.acc = Account()
    # test successful signup
    def test_models_adduser_method_returns_correct_result(self):
        result = self.acc.adduser("name", "email", "password", "password")
        self.assertEqual(True, result)
    # test unseccessful signup
    def test_models_adduser_method_returns_appropriate_for_password_mismatch(self):
        result = self.acc.adduser("name", "email", "password", "mismatched")
        self.assertTrue("pass_fail", result)
    # test user existence
    def test_models_adduser_method_returns_false_for_existing_user_registration(self):
        self.acc.adduser("name", "email", "password", "password")
        result = self.acc.adduser("name", "email", "password", "password")
        self.assertEqual(False, result)
    # test login failure
    def test_models_login_method_returns_wrong_result(self):
        result = self.acc.login("name", "password")
        self.assertFalse("success" == result)
if __name__ == '__main__':
    unittest.main()
    
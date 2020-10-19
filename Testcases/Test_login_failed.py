#system, driver modules
import sys
sys.path.append('.')
import time
import unittest

#import other modules
from Testcases.BaseTestcase import BaseTestcase
from Testdata.Data import LoginData
from Pages.LoginPage import LoginPage
from Pages.LoginResultPage import LoginResultPage
from Objects.Account import Account
from Locators.LoginPage import LoginPageLocators
from Locators.LoginResultPage import LoginResultPageLocators

class LoginFailed(BaseTestcase):
  @classmethod
  def setUp(self):
    super().setUp()
    self.login_page = LoginPage(self.driver)
    self.result_page = LoginResultPage(self.driver)
    self.user = Account('','')
    # self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
    print('hi Tien')

  # def test_login_banned_user(self):
  #   self.user = Account(LoginData.BANNED_USER.get('username'), LoginData.BANNED_USER.get('password'))
  #   # self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
  #   self.login_page.login(self.user)
  #   self.assertIn(LoginData.BANNED_USER_MESSAGE, self.result_page.get_message())

  # def test_login_blank(self):
  #   # self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
  #   self.login_page.click_button_login(self.user)
  #   self.assertIn(LoginData.INVALID_USER_MESSAGE, self.result_page.get_message())

  def test_login_blank_username(self):
    print('laypass',LoginData.STANDARD_USER.get('password'))
    # self.enter_password(LoginData.STANDARD_USER.get('password')) => sai cho nay
    print('lay pass')
    # self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
    self.login_page.login(self.user)
    print('da login')
    self.assertIn(LoginData.USERNAME_REQUIRED_MESSAGE, self.result_page.get_message())
    time.sleep(2)

  '''def test_login_blank_password(self):
    self.user = Account(LoginData.STANDARD_USER.get('username'), '')
    # self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
    self.login_page.login(self.user)
    self.assertIn(LoginData.PASSWORD_REQUIRED_MESSAGE, self.result_page.get_message())

  def test_login_invalid_user(self):
    self.user = Account(LoginData.FAKE_USER.get('username'), LoginData.FAKE_USER.get('password'))
    # self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
    self.login_page.login(self.user)
    self.assertIn(LoginData.INVALID_USER_MESSAGE, self.result_page.get_message())

  def test_login_invalid_username(self):
    self.user = Account(LoginData.FAKE_USER.get('username'), LoginData.STANDARD_USER.get('password'))
    # self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
    self.login_page.login(self.user)
    self.assertIn(LoginData.INVALID_USER_MESSAGE, self.result_page.get_message())

  def test_login_invalid_password(self):
    self.user = Account(LoginData.STANDARD_USER.get('username'), LoginData.FAKE_USER.get('password'))
    self.login_page.login(self.user)
    self.assertIn(LoginData.INVALID_USER_MESSAGE, self.result_page.get_message())'''

  @classmethod
  def tearDown(self):
    super().tearDown()

if __name__ == '__main__':
    unittest.main()
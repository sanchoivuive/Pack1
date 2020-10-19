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

class Login(BaseTestcase):
  
  @classmethod
  def setUp(self):
    super().setUp()
    self.login_page = LoginPage(self.driver)
    self.result_page = LoginResultPage(self.driver)
    # print('hi Tien')

  def test_login_standard_user(self):
    #constructor
    # login_page = LoginPage(self.driver)
    # result_page = LoginResultPage(self.driver)
    user = Account(LoginData.STANDARD_USER.get('username'), LoginData.STANDARD_USER.get('password'))

    #check the right title of login page
    self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
    self.login_page.login(user)

    # check the right title of result page
    self.assertTrue(self.result_page.check_title(LoginData.PAGE_TITLE))
    self.assertIn('Products', self.result_page.get_header_title())
    # time.sleep(1)

  def test_login_glitch_user(self):
    user = Account(LoginData.GLITCH_USER.get('username'), LoginData.GLITCH_USER.get('password'))

    #check the right title of login page
    self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
    self.login_page.login(user)

    # check the right title of result page
    self.assertTrue(self.result_page.check_title(LoginData.PAGE_TITLE))
    self.assertIn('Products', self.result_page.get_header_title())
    time.sleep(1)

  def test_login_problem_user(self):
    user = Account(LoginData.PROBLEM_USER.get('username'), LoginData.PROBLEM_USER.get('password'))

    # check the right title of login page
    self.assertTrue(self.login_page.check_title(LoginData.PAGE_TITLE))
    self.login_page.login(user)

    # check the right title of result page
    self.assertTrue(self.result_page.check_title(LoginData.PAGE_TITLE))
    self.assertIn('Products', self.result_page.get_header_title())
    time.sleep(1)

  @classmethod
  def tearDown(self):
    super().tearDown()

if __name__ == '__main__':
  unittest.main()

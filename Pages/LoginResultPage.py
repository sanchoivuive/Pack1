from Pages.BasePage import BasePage
from Locators.LoginResultPage import LoginResultPageLocators

class LoginResultPage(BasePage):
  def __init__(self,driver):
    super().__init__(driver)

  def get_header_title(self):
    return self.get_text(LoginResultPageLocators.HEADER_TITLE)
  
  def get_url(self):
    return self.driver.current_url

  def get_message(self):
    return self.get_text(LoginResultPageLocators.LABEL_MESSAGE)
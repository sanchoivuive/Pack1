class Data():
  BASE_URL = "https://the-internet.herokuapp.com/login"
  USERNAME = "tomsmith"
  FAKE_USERNAME = "tien"
  PASSWORD = "SuperSecretPassword!"
  FAKE_PASSWORD = "SSecretPass"
  BROWSER = "chrome"

class LoginData():
  BASE_URL = 'https://www.saucedemo.com/'
  PAGE_TITLE = 'Swag Labs'
  LOGGED_IN_URL = 'https://www.saucedemo.com/inventory.html'
  STANDARD_USER = {'username': 'standard_user', 'password': 'secret_sauce'}
  FAKE_USER = {'username': 'tienaaa', 'password': 'hello_world'}
  PROBLEM_USER = {'username': 'problem_user', 'password': 'secret_sauce'}
  GLITCH_USER = {'username': 'performance_glitch_user', 'password': 'secret_sauce'}
  BANNED_USER = {'username': 'locked_out_user', 'password': 'secret_sauce'}
  BANNED_USER_MESSAGE = 'Sorry, this user has been locked out.'
  INVALID_USER_MESSAGE = 'Username and password do not match any user in this service'
  USERNAME_REQUIRED_MESSAGE = 'Username is required'
  PASSWORD_REQUIRED_MESSAGE = 'Password is required'

class Browsers():
  CHROME = 'Chrome'
  FIREFOX = 'Firefox'
  OPERA = 'Opera'
  EDGE = 'Edge'
  SAFARI = 'Safari'
  PHANTOMJS = 'PhantomJS'



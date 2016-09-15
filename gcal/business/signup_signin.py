from pages.loginpage import LoginPage
import time

class SignUpSignIn(object):

    def login(self, driver, username, password):
        loginpage = LoginPage(driver)
        loginpage.enter_email(driver, username)
        loginpage.click_on_next(driver)
        time.sleep(10)
        loginpage.enter_password(driver, password)
        homepage = loginpage.click_on_signin(driver)
        return homepage




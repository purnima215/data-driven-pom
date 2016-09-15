
from page import Page
from page import InvalidPageError
from homepage import HomePage
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

class LoginPage(Page):

    """This covers the Login page region."""

    _login_page_title = "Google Calendar"

    email_textbox = lambda self:self.locate_id("Email")
    next_button = lambda self:self.locate_id("next")
    password_textbox = lambda self:self.locate_id("Passwd")
    submit_button = lambda self:self.locate_id("signIn")

    def _validate_page(self, driver):
        '''Validates if it is Tags Page that is currently opened.'''
        if driver.title != self._login_page_title:
            #self.is_error_present_on_opened_page(driver)
            raise InvalidPageError("This is not Google Login Page. Currently at %s" %(driver.current_url))

    def enter_email(self, driver, email):
        """Enters the email in the emailbox"""
        self.email_textbox().clear()
        self.email_textbox().send_keys(email)

    def enter_password(self, driver, password):
        """Enter the password in the password box"""
        self.password_textbox().clear()
        self.password_textbox().send_keys(password)

    def click_on_next(self, driver):
        self.next_button().click()

    def click_on_signin(self, driver):
        self.submit_button().click()
        time.sleep(10)
        return HomePage(driver)


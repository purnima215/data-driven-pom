
#BasePage

import abc
from selenium.common.exceptions import NoAlertPresentException, ElementNotVisibleException,\
    NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

class Page(object):

    """This is the super class for all the Pages. It contains all the wrappers for locators, any common functionality that is across
    pages and custom defined exceptions"""

    webdriver = None

    def __init__(self, webdriver, log = None):
        """Constructor for Page Object."""
        if log == None:
        #instantiate the logger
            pass
        else:
            self.log = log
        self._validate_page(webdriver)
        self.webdriver = webdriver

    def locate_id(self, locator):
        element = self.webdriver.find_element_by_id(locator)
        if element:
            return element
        else:
            raise NoSuchElementException

    def locate_multiple_classname(self, locator):
        """Wrapper for finding elements by classname"""
        element = self.webdriver.find_elements_by_class_name(locator)
        if element:
            return element
        else:
            raise NoSuchElementException

    def locate_xpath(self, locator):
        """Wrapper for finding element by xpat"""
        element = self.webdriver.find_element_by_xpath(locator)
        if element:
            return element
        else:
            raise NoSuchElementException

    @abc.abstractmethod
    def _validate_page(self, webdriver):
        """
        Perform checks to validate this page is the correct target page.

        @raise IncorrectPageException: Raised when we try to assign the wrong page to this page object.
        """
        return

    def select_by_visible_text_in_dropdown(self, dropdown_html_id,
                                               visible_text):
        dropdown_values = Select(self.locate_id(dropdown_html_id))
        dropdown_values.select_by_visible_text(visible_text)

    def click_checkbox_with_id(self, html_id_for_checkbox, check = True):
        try:
            check_box = self.locate_id(html_id_for_checkbox)
        except NoSuchElementException, e:
            self.log.debug(e)
            return
        except Exception, e:
            self.log.debug(e)
            return
        if check:
            if not check_box.is_selected():
                #self.log.info("Checkbox is not already checked. Checking it now.")
                check_box.click()
        else:
            if check_box.is_selected():
                #self.log.info("Checkbox is already checked. Un-checking it now.")
                check_box.click()

class InvalidPageError(Exception):
    '''Thrown when tried to instantiate the incorrect page to a Page object.'''

class InvalidOptionError(Exception):
    '''Thrown when tried when invalid option is given as input.'''


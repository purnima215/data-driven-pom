# import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os, time
import unittest
from business.signup_signin import SignUpSignIn

def screenGrabFile(driver, self):
    from datetime import datetime
    current_date = str(datetime.now()).replace(" ", "_").replace(":", "-")

    screenGrabFile = "%s%s%s.png" % ("/tmp/", self.__class__.__name__, current_date)
    # print "Current url is %s - %s" % (driver.current_url, driver.title)
    # print "Saving screen in %s" % (screenGrabFile)
    # driver.get_screenshot_as_file(screenGrabFile)


class BaseTest(unittest.TestCase):
    def __init__(self, methodName='runTest', log=None, proxy=False):
        print "IN init of setBrowser"
        self.driver = None
        self.startTime = 0
        self.endTime = 0
        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        # This method can be modified to read the browser to run from a config file and run the browser that has been asked for.
        self.driver = webdriver.Chrome('C:\Users\PURNIMA\Documents\chromedriver')
        self.driver.get("https://calendar.google.com")
        self.driver.implicitly_wait(70)

    def login(self):
        loginpage = SignUpSignIn()
        return loginpage.login(self.driver, username="purnima.dummy@gmail.com", password="sushmitha")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

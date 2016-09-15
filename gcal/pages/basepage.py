from page import Page
import time

class BasePage(Page):

    webdriver = Page.webdriver

    @property
    def header(self):
       # """Defines the header region that is common across the pages."""
        return BasePage.HeaderRegion(self.webdriver)

    @property
    def footer(self):
        pass

    def _validate_page(self, webdriver):
        pass

    class HeaderRegion(Page):

        # Menu items
        settings_menu = lambda self: self.locate_id("mg-settings")

        #Options in Settings.
        settings_option = lambda self: self.locate_xpath("//*[@id=':k']/div")

        def expand_settings_menu(self, driver):
            """Clicks on the Tags menu in the header region."""
            # self.log.debug("About to click on the tags menu")
            self.settings_menu().click()
            time.sleep(5)

        def click_on_settings_in_menu(self, driver):
            self.settings_option().click()
            from pages.settings_page import SettingsPage
            return SettingsPage(driver)

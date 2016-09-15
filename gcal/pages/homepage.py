from basepage import BasePage
from page import InvalidPageError

class HomePage(BasePage):
    _home_page_title = "Google Calendar - Week of Sep 12, 2016"

    time_column_classname = lambda self: self.locate_multiple_classname("tg-time-pri")

    def _validate_page(self, driver):
        '''Validates if it is Tags Page that is currently opened.'''
        if driver.title != self._home_page_title:
            # self.is_error_present_on_opened_page(driver)
            print driver.title
            raise InvalidPageError("This is not Google Home Page. Currently at %s" % (driver.current_url))

    def get_values_in_time_column(self, driver):
        time_cells = self.time_column_classname()
        time_values = [cell.text for cell in time_cells]
        return time_values

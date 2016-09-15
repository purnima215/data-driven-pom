from basepage import BasePage
from page import InvalidPageError, InvalidOptionError

class SettingsPage(BasePage):

    _settings_page_title = "Google Calendar - Week of Sep 12, 2016"

    timeformat_dropdown_id = "format24HourTime"
    week_start_day_id = "firstDay"
    event_duration_id = ":y.lw"
    speedy_event_checkbox = ":y.sw"

    save_button = lambda self:self.locate_id("settings_save_btn")

    start_days_valid_options = ["Sunday", "Monday", "Saturday"]
    timeformat_valid_options = ["12hr", "24hr"]

    def _validate_page(self, driver):
        '''Validates if it is Tags Page that is currently opened.'''
        if driver.title != self._settings_page_title:
            print driver.title
            #self.is_error_present_on_opened_page(driver)
            raise InvalidPageError("This is not Google Calendar Settings Page. Currently at %s" %(driver.current_url))

    def choose_time_format(self, driver, format = "12hr"):
        if format not in self.timeformat_valid_options:
            raise InvalidOptionError
        if format == "12hr":
            format = "1:00pm"
        else:
            format = "13:00"
        self.select_by_visible_text_in_dropdown(self.timeformat_dropdown_id, format)

    def choose_week_start_day(self, driver, firstday = "Monday"):
        if firstday not in self.start_days_valid_options:
            raise InvalidOptionError
        self.select_by_visible_text_in_dropdown(self.week_start_day_id, firstday)

    def choose_event_duration(self, driver, duration):
        self.select_by_visible_text_in_dropdown(self.event_duration_id, duration)

    def select_speedy_event_checkbox(self, driver, speedy = True):
        self.click_checkbox_with_id(self.speedy_event_checkbox, speedy)

    def click_save_button(self, driver):
        self.save_button().click()
        from homepage import HomePage
        return HomePage(driver)

from pages.homepage import HomePage
from pages.settings_page import SettingsPage

class Settings(object):
    def __init__(self):
        pass

    def set_time_format(self, driver, homepage_obj, timeformat):
        homepage_obj.header.expand_settings_menu(driver)
        settingspage = homepage_obj.header.click_on_settings_in_menu(driver)
        settingspage.choose_time_format(driver, timeformat)
        homepage_obj = settingspage.click_save_button(driver)
        return homepage_obj

    def get_time_values_on_homepage(self, driver, homepage_obj):
        time_values = homepage_obj.get_values_in_time_column(driver)
        return time_values


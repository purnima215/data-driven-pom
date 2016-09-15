from business.settings import Settings
from basetest import BaseTest

class Test12hourTimeFormat(BaseTest):

    def __init__(self, methodName = 'runTest', log=None):
        BaseTest.__init__(self)

    def runTest(self):
        home_page = self.login()
        settings = Settings()
        if home_page:
            home_page = settings.set_time_format(self.driver, home_page, "12hr")
            time_values = settings.get_time_values_on_homepage(self.driver, home_page)
            print time_values
            time_values = [time_value[-2:] for time_value in time_values]
            print time_values
            for time in time_values:
                self.assertIn(time, ["am", "pm"])
        else:
            print "homepage is null."
            print home_page





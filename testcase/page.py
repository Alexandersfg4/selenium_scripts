

class BaseBage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BaseBage):
    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element()
        element.clck()
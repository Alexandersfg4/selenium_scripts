import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome('/Users/aleksandrbortnikov/Documents/WebDrivers/chromedriver')
        self.driver.get("http:www.python.org")

    #the method will run automaticly because of the begining test_
    def test_example(self):
        print("Test")
        assert True

    def test_tittle(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matches()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
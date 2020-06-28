import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://helion.pl/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
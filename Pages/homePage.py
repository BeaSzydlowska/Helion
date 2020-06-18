from Pages.basePage import BasePage
from Locators.locators import HomePageLocators
# from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    def enter_searched_product(self, product):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(HomePageLocators.SEARCHER))
        searcher = self.driver.find_element(*HomePageLocators.SEARCHER)
        if searcher.is_enabled():
            searcher.clear()
            searcher.send_keys(product)
            searcher.submit()
        else:
            print("searcher field is disabled.")

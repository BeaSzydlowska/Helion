from Pages.basePage import BasePage
from Locators.locators import HomePageLocators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    def enter_searched_product(self, product):
        """umożliwia wprowadzenie tekstu w okno wyszukiwarki i zatwierdzenie wyszukania"""
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(HomePageLocators.SEARCHER))
        searcher = self.driver.find_element(*HomePageLocators.SEARCHER)
        if searcher.is_enabled():
            searcher.clear()
            searcher.send_keys(product)
            searcher.submit()
        else:
            print("searcher field is disabled.")

    def return_to_home_page(self):
        """umożliwia powrót do strony głównej"""
        self.driver.get('https://helion.pl/')
        title = self.driver.title
        print(title)
        #Księgarnia internetowa informatyczna Helion.pl - wydawnictwo informatyczne, książki, kursy
        return title

    def go_to_basket(self):
        """umożliwia kliknięcie w Koszyk"""
        self.driver.find_element(*HomePageLocators.GO_TO_BASKET).click()

    def go_to_register_page(self):
        """umożliwia przekirrowanie do strony rejestracji"""
        account_btn = self.driver.find_element(*HomePageLocators.ACCOUNT_BTN)
        webdriver.ActionChains(self.driver).move_to_element(account_btn).perform()
        register = self.driver.find_element(*HomePageLocators.REGISTER_BTN)
        register.click()

    def go_to_login_page(self):
        """umożliwia przekirrowanie do strony logowania"""
        account_btn = self.driver.find_element(*HomePageLocators.ACCOUNT_BTN)
        webdriver.ActionChains(self.driver).move_to_element(account_btn).perform()
        register = self.driver.find_element(*HomePageLocators.LOGIN_BTN)
        register.click()

    def accept_cookie_policy(self):
        """umożliwia akceptacje cookie"""
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located(HomePageLocators.COOKIE))
        cookie = self.driver.find_element(*HomePageLocators.COOKIE)
        cookie.click()

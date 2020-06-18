from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.basePage import  BasePage
from Locators.locators import HomePageLocators
from Locators.locators import SearchPageLocators
from Locators.locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class ProductPage(BasePage):

    def product_title(self):
        title = self.driver.find_element(*ProductPageLocators.TITLE)
        return title.text

    def choose_ebook_option(self):
        ebook_box = self.driver.find_element(*ProductPageLocators.EBOOK_BOX)
        if ebook_box.is_selected():
            print("eboo wybrano")
            pass
        else:
            ebook_box.click()
        sleep(10)

    def add_ebook_to_basket(self):
        self.driver.find_element(*ProductPageLocators.ADD_EBOOK_TO_BASKET).click()
        sleep(5)

    # NIE WIEM JAK TO ZROBIC- Z DEFAULTA TO JEST ZAWSZE TA OPCJA !!!! I NIE UMIEM SOBIE OKRESLIC CZY TO JEST WYBRANE CZY NIE
    # def choose_book_option(self):
    #     book_box = self.driver.find_element(*ProductPageLocators.BOOK_BOX)
    #     if book_box.is_selected():
    #         print("wybrano juz te opcje")
    #
    #         pass
    #     else:
    #         book_box.click()
    #     sleep(10)

    def add_book_to_basket(self):
        self.driver.find_element(*ProductPageLocators.ADD_BOOK_TO_BASKET).click()
        sleep(15)

    def enter_book_quantity(self, quantity):
        print("wchodze do quantity")
        WebDriverWait(self.driver, 10).until((EC.presence_of_element_located(ProductPageLocators.BOOK_QUANTITY)))
        amount_button = self.driver.find_element(*ProductPageLocators.BOOK_QUANTITY)
        amount_button.clear()
        print("wyczyscilam")
        sleep(10)
        amount_button.send_keys(quantity)
        if quantity >10:
            amount_button.clear()
            return "Wartość nie może być większa niż 10"
        else:
            return quantity


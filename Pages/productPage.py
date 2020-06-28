from Pages.basePage import BasePage
from Locators.locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class ProductPage(BasePage):

    def product_title(self):
        """returns product title"""
        title = self.driver.find_element(*ProductPageLocators.TITLE)
        return title.text

    def enter_book_quantity(self, quantity):
        """allows to enter the quantity for books"""
        WebDriverWait(self.driver, 10).until((EC.presence_of_element_located(ProductPageLocators.BOOK_QUANTITY)))
        amount_button = self.driver.find_element(*ProductPageLocators.BOOK_QUANTITY)
        amount_button.clear()
        amount_button.send_keys(quantity)
        if quantity > 10:
            amount_button.clear()
            return "The value cannot be greater than 10"
        else:
            return quantity

    def add_to_cart(self):
        """allows to add a product to the cart regardless of the type of product"""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART))
        button = self.driver.find_element(*ProductPageLocators.ADD_TO_CART)
        button.click()

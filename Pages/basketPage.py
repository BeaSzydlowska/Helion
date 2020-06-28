from Pages.basePage import BasePage
from Locators.locators import BasketPageLocators
from time import sleep


class BasketPage(BasePage):

    def return_len_products_in_basket(self):
        """returns length of the product's in the basket list"""
        rows = self.driver.find_elements(*BasketPageLocators.ROWS)
        productList = []
        for row in rows:
            productList.append(row)
        return len(rows)

    def check_product_name_in_cart(self):
        """returns product's title in the basket"""
        rows = self.driver.find_elements(*BasketPageLocators.ROWS)
        sleep(5)
        for row in rows:
            name = row.find_element_by_xpath("//td[@class='desc']//h2/a")
            return name.text

    def check_quantity_of_selected_product(self, product):
        """returns quantity of selected product"""
        rows = self.driver.find_elements(*BasketPageLocators.ROWS)
        for row in rows:
            name = row.find_element_by_xpath("//td[@class='desc']//h2/a")
            if name.text in product:
                amount = row.find_element_by_xpath("//td[@class='amount']//input[@class = 'ilosc']")
                amount = amount.get_attribute("value")
                return int(amount)

    def select_checkbox(self, product):
        """allows to select checkbox by product's title"""
        rows = self.driver.find_elements(*BasketPageLocators.ROWS)
        for row in rows:
            name = row.find_element_by_xpath("td[@class='desc']//h2/a")
            if product in name.text:
                checkbox = row.find_element_by_xpath("td/div/label/span[@class='input']")
                checkbox.click()

    def click_remove_selected(self):
        """allows to click on "Usuń zaznaczone"linked text"""
        remove_btn = self.driver.find_element(*BasketPageLocators.REMOVE)
        remove_btn.click()
        # sleep(5)
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()

    def remove_results(self):
        """returns basket's content after removing products.If basket is empty  - returns "Koszyk jest pusty" string.
        If basket is not empty - returns list of products in the basket."""
        try:
            napis = self.driver.find_element(*BasketPageLocators.EMPTY_BASKET)
            return napis.text
        except:
            list_of_products = []
            rows = self.driver.find_elements(*BasketPageLocators.ROWS)
            for row in rows:
                name = row.find_element_by_xpath("//td[@class='desc']//h2/a")
                list_of_products.append(name.text)
                return list_of_products

    def select_all_products(self):
        """allows to select all products in cart"""
        select_all_btn = self.driver.find_element(*BasketPageLocators.SELECT_ALL)
        select_all_btn.click()

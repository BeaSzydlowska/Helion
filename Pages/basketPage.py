from Pages.basePage import BasePage
from Locators.locators import BasketPageLocators
from time import sleep


class BasketPage(BasePage):

    def return_len_products_in_basket(self):
        """umozliwia zwrócenie długosci listy produktów w koszyku"""
        rows = self.driver.find_elements(*BasketPageLocators.ROWS)
        productList = []
        for row in rows:
            productList.append(row)
        return len(rows)

    def check_product_name_in_cart(self):
        """umożliwia zwrócenie tytułu produktu znajdującego sie w koszyku"""
        rows = self.driver.find_elements(*BasketPageLocators.ROWS)
        for row in rows:
            name = row.find_element_by_xpath("//td[@class='desc']//h2/a")
            return name.text

    def check_quantity_of_selected_product(self, product):
        """umożliwia zwrócenie ilości sztuk wybranego produktu"""
        rows = self.driver.find_elements(*BasketPageLocators.ROWS)
        for row in rows:
            name = row.find_element_by_xpath("//td[@class='desc']//h2/a")
            if name.text in product:
                amount = row.find_element_by_xpath("//td[@class='amount']//input[@class = 'ilosc']")
                amount = amount.get_attribute("value")
                return int(amount)


    def check_checkbox(self, product):
        """umożliwia zaznaczenie wybranego checkboxa po tytule"""
        rows = self.driver.find_elements(*BasketPageLocators.ROWS)
        for row in rows:
            name = row.find_element_by_xpath("td[@class='desc']//h2/a")
            if product in name.text:
                checkbox = row.find_element_by_xpath("td/div/label/span[@class='input']")
                checkbox.click()


    def click_remove_selected(self):
        """umożliwia klikniecie w "Usuń zaznaczone"""
        remove_btn = self.driver.find_element(*BasketPageLocators.REMOVE)
        remove_btn.click()
        # sleep(5)
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()

    def remove_results(self):
        """zwraca zwartość koszyka po usunieciu produktów. Jesli koszyk został opróżniony - zwaraca napis "Koszyk jest pusty.
        Jesli w koszyku pozostały produkty - zwaraca liste produktów pozostałych w koszyku"""
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
        """umożliwia zaznaczenie wszystkich pozycji w koszyku"""
        select_all_btn = self.driver.find_element(*BasketPageLocators.SELECT_ALL)
        select_all_btn.click()

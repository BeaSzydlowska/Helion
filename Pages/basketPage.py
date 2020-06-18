from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.basePage import  BasePage
from Locators.locators import HomePageLocators
from Locators.locators import SearchPageLocators
from Locators.locators import ProductPageLocators
from Locators.locators import BasketPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class BasketPage(BasePage):
    def check_product_name_in_cart(self):
        rows = self.driver.find_elements(*BasketPageLocators.ROWS)
        for row in rows:
            name = row.find_element_by_xpath("//td[@class='desc']//h2/a")
            print(name.text)
            return name.text
            sleep(10)


    def check_quantity_of_selected_product(self, product):
        rows = self.driver.find_elements(*BasketPageLocators.ROWS)
        for row in rows:
            name = row.find_element_by_xpath("//td[@class='desc']//h2/a")

            if name.text in product:
                amount = row.find_element_by_xpath("//td[@class='amount']//input[@class = 'ilosc']")
                amount = amount.get_attribute("value")
                print(amount)
            return int(amount)


    def check_checkbox(self,product):
        rows = self.driver.find_elements(*BasketPageLocators.ROWS)
        for row in rows:
            name = row.find_element_by_xpath("//td[@class='desc']//h2/a")
            if name.text in product:
                checkbox = row.find_element_by_xpath("//td[@class='checkbox']")
                checkbox.click()
                if checkbox.is_selected():
                    i = True
                else:
                    i = False

            print(i)




    def click_remove_selected(self):
        remove_btn = self.driver.find_element(*BasketPageLocators.REMOVE)
        remove_btn.click()
        sleep(5)
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()
        sleep(5)



    def remove_results(self):
        try:
            napis = self.driver.find_element(*BasketPageLocators.EMPTY_BASKET)
            print(napis.text)
            return napis.text

        except:
            list_of_products = []
            rows = self.driver.find_elements(*BasketPageLocators.ROWS)
            for row in rows:
                # list_of_products = []
                name = row.find_element_by_xpath("//td[@class='desc']//h2/a")
                print(name.text)
                list_of_products.append(name.text)
                print(list_of_products)
                return list_of_products




    def select_all_products(self):
        select_all_btn = self.driver.find_element(*BasketPageLocators.SELECT_ALL)
        select_all_btn.click()
        rows = self.driver.find_elements(*BasketPageLocators.ROWS)
        i = True
        for row in rows:
            checkbox = row.find_element_by_xpath("//td[@class='checkbox']")
            if checkbox.is_selected():
                i = True
            else:
                i = False

        print(i)





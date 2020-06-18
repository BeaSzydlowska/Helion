
from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.basePage import  BasePage
from Locators.locators import HomePageLocators
from Locators.locators import SearchPageLocators
from Locators.locators import ProductPageLocators
from time import sleep



#tutaj musi byc rezultat wyszukania :
#albo lista
#albo nic

product = "Python dla każdego. Podstawy programowania. Wydanie III Michael Dawson"
class SearchPage(BasePage):
    """
    Klasa bazowa dla każdej strony
    """

    def search_results(self):
        try:
            napis = self.driver.find_element(*SearchPageLocators.NO_SEARCH_RESULTS)
            # print(napis.text)
            return napis.text
        except:
            lista = self.driver.find_elements(*SearchPageLocators.LIST_OF_SEARCHED_PRODUCTS)
            lista_names = self. driver.find_elements(*SearchPageLocators.LIST_OF_NAMES)
            print(len(lista))
            list_of_returned_titles = []
            for title in lista_names:
                print(title.text)
                list_of_returned_titles.append(title.text)
            print(list_of_returned_titles)
            return list_of_returned_titles



    def choose_product_from_list(self, index):
        # lista = self.driver.find_elements(*SearchPageLocators.LIST_OF_SEARCHED_PRODUCTS)
        # # print(len(lista))
        # # lista[0].click()
        # # sleep(5)
        # # for element in lista:
        # #     button = element.find_element(By.XPATH, "//img")
        # #     button.click()
        # #     sleep(5)
        names_of_searched_products = self.driver.find_elements(*SearchPageLocators.LIST_OF_NAMES)
        names_of_searched_products[index].click()

    def clikc_add_to_cart_on_searched_results(self):
        buton = self.driver.find_elements(*SearchPageLocators.ADD_TO_CART_BTN)
        print(len(buton))
        buton[0].click()
        sleep(5)


    def add_to_basket_as_book(self):
        button = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BOOK)
        button.click()
        sleep(5)


    #
    # # TO SA JUZ TESTY KOSZYKA
    # def check_lenght_list_of_product_in_cart(self):
    #     rows = self.driver.find_elements(*HomePageLocators.ROWS)
    #     print(len(rows))
    #
    # def check_product_in_cart(self):
    #     rows = self.driver.find_elements(*HomePageLocators.ROWS)
    #     for row in rows:
    #         name =row.find_element_by_xpath("//td[@class='desc']//h2/a")
    #         print(name.text)
    #         sleep(10)
    #
    # def check_checkbox(self,product):
    #     rows= self.driver.find_elements(*HomePageLocators.ROWS)
    #     for row in rows:
    #         name = row.find_element_by_xpath("//td[@class='desc']//h2/a")
    #         if name.text in product:
    #             row.find_element_by_xpath("//td[@class='checkbox']").click()
    #
    #         sleep(10)
    #
    # def remove_selected(self):
    #     remove_btn = self.driver.find_element(*HomePageLocators.REMOVE)
    #     remove_btn.click()
    #     sleep(5)
    #     alert_obj = self.driver.switch_to.alert
    #     alert_obj.accept()
    #     sleep(5)
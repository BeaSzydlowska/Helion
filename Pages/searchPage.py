from Pages.basePage import  BasePage
from Locators.locators import SearchPageLocators


class SearchPage(BasePage):

    def search_results_is_not_empty(self):
        """umożliwia sprawdzenie czy lista wyników nie jest pusta"""
        try:
            napis = self.driver.find_element(*SearchPageLocators.NO_SEARCH_RESULTS)
            return False
        except:
            return True

    def display_message_when_search_results_are_empty(self):
        """dla braku wyników wyszukiwań zwraca napis "Nie znaleziono szukanej frazy" """
        napis = self.driver.find_element(*SearchPageLocators.NO_SEARCH_RESULTS)
        return napis.text

    def verify_if_sorting_by_best_match_is_set_as_default(self):
        """sprawdza czy wyniki wyszukiwania sa posortowane po "Najlepiej pasujące" """
        sorting_option_selected = self.driver.find_element(*SearchPageLocators.SORTING_DEFAULT)
        if sorting_option_selected.text == "Najlepiej pasujące":
            return True
        else:
            return False

    def return_list_of_titles_searched_results(self):
        """zwraca wyniki wyszukiwań gdy lista wyników nie jest pusta"""
    #    lista = self.driver.find_elements(*SearchPageLocators.LIST_OF_SEARCHED_PRODUCTS)
        lista_names = self.driver.find_elements(*SearchPageLocators.LIST_OF_NAMES)
        list_of_returned_titles = []
        for title in lista_names:
            print(title.text)
            list_of_returned_titles.append(title.text)
        return list_of_returned_titles

    def choose_product_from_list(self, index):
        """umożliwia kliknięcie wybranego produktu po zadanym indeksie listy"""
        names_of_searched_products = self.driver.find_elements(*SearchPageLocators.LIST_OF_NAMES)
        names_of_searched_products[index].click()

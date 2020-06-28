from Pages.basePage import BasePage
from Locators.locators import SearchPageLocators


class SearchPage(BasePage):

    def search_results_is_not_empty(self):
        """allows checking if the result list is not empty"""
        try:
            message = self.driver.find_element(*SearchPageLocators.NO_SEARCH_RESULTS)
            return False
        except:
            return True

    def display_message_when_search_results_are_empty(self):
        """for no search results returns "Nie znaleziono szukanej frazy" string """
        message = self.driver.find_element(*SearchPageLocators.NO_SEARCH_RESULTS)
        return message.text

    def verify_if_sorting_by_best_match_is_set_as_default(self):
        """checks if search results are sorted by"Najlepiej pasujące" """
        sorting_option_selected = self.driver.find_element(*SearchPageLocators.SORTING_DEFAULT)
        if sorting_option_selected.text == "Najlepiej pasujące":
            return True
        else:
            return False

    def return_list_of_titles_searched_results(self):
        """returns search results if the results list is not empty"""
        lista_names = self.driver.find_elements(*SearchPageLocators.LIST_OF_NAMES)
        list_of_returned_titles = []
        for title in lista_names:
            print(title.text)
            list_of_returned_titles.append(title.text)
        return list_of_returned_titles

    def choose_product_from_list(self, index):
        """allows to choose selected product by the given list index"""
        names_of_searched_products = self.driver.find_elements(*SearchPageLocators.LIST_OF_NAMES)
        names_of_searched_products[index].click()

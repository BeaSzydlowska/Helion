import csv

from Tests.baseTest import BaseTest
from Pages.homePage import HomePage
from Pages.searchPage import SearchPage
from Pages.productPage import ProductPage
import unittest
from ddt import ddt, data, unpack


def get_data(file_name):
    rows = []
    data_file = open(file_name, 'rt')
    reader = csv.reader(data_file)
    next(reader, 1)
    for row in reader:
        rows.append(row)
    return rows


@ddt
class SearchTest(BaseTest):
    """ Testy związane z wyszukiwaniem produktów """

    def test_searchNonExistingProduct(self):
        """Sprawdzenie poprawności wyszukiwania produktów za pośrednictwem okienka wyszukiwania
        z podaniem danych niepoprawnych (nieistniejących w bazie)"""
        product = "fdsgdsggd"
        hp = HomePage(self.driver)
        hp.enter_searched_product(product)
        sp = SearchPage(self.driver)
        results = sp.search_results_is_not_empty()
        if self.assertFalse(results, "There is a product on a list"):
            info = sp.display_message_when_search_results_are_empty()
            self.assertEqual(info, "Nie znaleziono szukanej frazy", "Product exist in our database")

    @data(*get_data("producttitles.csv"))
    @unpack
    def test_03_searching_by_title(self, product):
        """Sprawdzenie poprawności wyszukiwania produktów za pośrednictwem okienka wyszukiwania
        z podaniem istniejącego dokładnego tytułu"""
        hp = HomePage(self.driver)
        hp.enter_searched_product(product)
        sp = SearchPage(self.driver)
        results = sp.search_results_is_not_empty()
        self.assertTrue(results, "There is no product on a list")
        default_sorting = sp.verify_if_sorting_by_best_match_is_set_as_default()
        self.assertTrue(default_sorting, "Sorting by best match is not set as default")
        sp.choose_product_from_list(0)
        pp = ProductPage(self.driver)
        title = pp.product_title()
        self.assertIn(product, title, "incorrect title")


if __name__ == "__main__":
    unittest.main()

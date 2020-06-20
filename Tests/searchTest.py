from Tests.baseTest import BaseTest
from Pages.homePage import HomePage
from Pages.searchPage import SearchPage
from Pages.productPage import ProductPage
import unittest

# hp.enter_searched_product("Python dla każdego. Podstawy programowania. Wydanie III Michael Dawson")
# hp.enter_searched_product("fdsgdsggd")
# hp.enter_searched_product("Python")
class SearchTest(BaseTest):
    """ Testy związane z wyszukiwaniem """
    # def test_search_non_existing_product(self):
    #     "wyszukiwanie pozycji, ktora nie istnieje w bazie - działa"
    #     product = "fdsgdsggd"
    #     hp = HomePage(self.driver)
    #     hp.enter_searched_product(product)
    #     sp = SearchPage(self.driver)
    #     results = sp.search_results()
    #     self.assertEqual(results, "Nie znaleziono szukanej frazy", "Product exist in our database")
    #

    # def test_phrase_searching(self):
    #     "wyszukiwanie pozycji po zadanej frazie -działa"
    #
    #     product = "Python"
    #     hp = HomePage(self.driver)
    #     hp.enter_searched_product(product)
    #     sp = SearchPage(self.driver)
    #     results = sp.search_results()
    #     for element in results:
    #         print (element)
    #         self.assertIn(product, element, "The search phrase was not found in the title")

    def test_title_search(self):
        product = "Python dla każdego. Podstawy programowania. Wydanie III"
        hp = HomePage(self.driver)
        hp.enter_searched_product(product)
        sp = SearchPage(self.driver)
        results = sp.search_results()
        # for element in results:
        #     print(element)
        #     self.assertIn(product, element, "The search phrase was not found in the title")
        sp.choose_product_from_list(0)
        pp = ProductPage(self.driver)
        title  = pp.product_title()
        self.assertIn(product, title, "incorrect title")






#     sp.search_product("Python dla każdego. Podstawy programowania. Wydanie III Michael Dawson")





















if __name__=="__main__":
    unittest.main(verbosity=2)

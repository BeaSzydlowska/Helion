from Tests.baseTest import BaseTest
from Pages.homePage import HomePage
from Pages.searchPage import SearchPage
from Pages.productPage import ProductPage
import unittest
class basketTest(BaseTest):
    # def test_costam(self):
    #     sp = SearchPage(self.driver)
    #     sp.search_product("Python dla każdego. Podstawy programowania. Wydanie III Michael Dawson")
    #     sp.choose_product_from_list()
    #     sp.add_to_basket_as_book()
    #     sp.check_product_in_cart()
    #     sp.check_checkbox("Python dla każdego. Podstawy programowania. Wydanie III Michael Dawson")
    #     sp.remove_selected()

    def test_add_selected_ebook_to_basket_from_product_page(self):
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
        title = pp.product_title()
        self.assertIn(product, title, "incorrect title")
        # pp.choose_ebook_option()
        # pp.enter_book_quantity(4)
        x = pp.enter_book_quantity(4)
        print(x)
        pp.add_book_to_basket()
        # pp.choose_ebook_option()
        # pp.add_book_to_basket()









if __name__=="__main__":
    unittest.main(verbosity=2)

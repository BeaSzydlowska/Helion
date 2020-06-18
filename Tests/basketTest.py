from Tests.baseTest import BaseTest
from Pages.homePage import HomePage
from Pages.basketPage import BasketPage
from Pages.searchPage import SearchPage
from Pages.productPage import ProductPage
import unittest
class basketTest(BaseTest):

    # def test_add_selected_book_to_basket_from_product_page_with_quantity(self):
    ##test działa !
    #     product = "Python dla każdego. Podstawy programowania. Wydanie III"
    #     quantity = 4
    #     hp = HomePage(self.driver)
    #     hp.enter_searched_product(product)
    #     sp = SearchPage(self.driver)
    #     results = sp.search_results()
    #     # for element in results:
    #     #     print(element)
    #     #     self.assertIn(product, element, "The search phrase was not found in the title")
    #     sp.choose_product_from_list(0)
    #     pp = ProductPage(self.driver)
    #     title = pp.product_title()
    #     self.assertIn(product, title, "incorrect title")
    #     x = pp.enter_book_quantity(quantity)
    #     print(x)
    #     pp.add_book_to_basket()
    #     # pp.choose_ebook_option()
    #     # pp.add_book_to_basket()
    #     bp= BasketPage(self.driver)
    #     product_name = bp.check_product_name_in_cart()
    #     self.assertIn(product, product_name,"Selected product not added to basket")
    #     amount = bp.check_quantity_of_selected_product(product)
    #     self.assertEqual(quantity, amount , "incorrect amount of added product")

    #
    # def test_remove_last_product_from_basket(self):
    # # DZIALA
    #     product = "Python dla każdego. Podstawy programowania. Wydanie III"
    #     quantity = 4
    #     hp = HomePage(self.driver)
    #     hp.enter_searched_product(product)
    #     sp = SearchPage(self.driver)
    #     sp.choose_product_from_list(0)
    #     pp = ProductPage(self.driver)
    #     title = pp.product_title()
    #     self.assertIn(product, title, "incorrect title")
    #     pp.add_to_cart()
    #     bp = BasketPage(self.driver)
    #     product_name = bp.check_product_name_in_cart()
    #     self.assertIn(product, product_name, "Selected product not added to basket")
    #     # bp.check_checkbox(product)
    #     bp.select_all_products()
    #     bp.click_remove_selected()
    #     bp.remove_results()
    #



 # def test_add_multiple_product_to_basket(self):
 #        """Test poprawnego dodania wielu produktów """
 #     product_list = []

    # def test_add_selected_videokurs_to_basket_from_product_page(self):
    # #test działa !
    #     product = "Frontend developer. Kurs video. HTML i CSS. Poziom średnio zaawansowany"
    #     hp = HomePage(self.driver)
    #     hp.enter_searched_product(product)
    #     sp = SearchPage(self.driver)
    #     sp.choose_product_from_list(0)
    #     pp = ProductPage(self.driver)
    #     title = pp.product_title()
    #     self.assertIn(product, title, "incorrect title")
    #     pp.add_to_cart()
    #     bp= BasketPage(self.driver)
    #     product_name = bp.check_product_name_in_cart()
    #     self.assertIn(product, product_name,"Selected product not added to basket")
    #
    # def test_add_selected_ebook_to_basket_from_product_page(self):
    # #test działa !
    #     product = "Frontend developer. Kurs video. HTML i CSS. Poziom średnio zaawansowany"
    #     hp = HomePage(self.driver)
    #     hp.enter_searched_product(product)
    #     sp = SearchPage(self.driver)
    #     sp.choose_product_from_list(0)
    #     pp = ProductPage(self.driver)
    #     title = pp.product_title()
    #     self.assertIn(product, title, "incorrect title")
    #     pp.add_to_cart()
    #     bp= BasketPage(self.driver)
    #     product_name = bp.check_product_name_in_cart()
    #     self.assertIn(product, product_name,"Selected product not added to basket")
    #
    #

    # def test_add_multiple_product_to_basket(self):
    #     """Test poprawnego dodania wielu produktów niezaleznie od rodzaju"""
    #     # DZIALA
    #     product_list = ["Frontend developer. Kurs video. HTML i CSS. Poziom średnio zaawansowany",
    #                  "Tysiąc szklanek herbaty. Spotkania na Jedwabnym Szlaku",
    #                  "English 4 IT. Praktyczny kurs języka angielskiego dla specjalistów IT i nie tylko"]
    #
    #     hp = HomePage(self.driver)
    #     sp = SearchPage(self.driver)
    #     pp = ProductPage(self.driver)
    #     bp = BasketPage(self.driver)
    #
    #     for product in product_list:
    #         hp.enter_searched_product(product)
    #         results = sp.search_results_is_not_empty()
    #         if results is True:
    #             sp.choose_product_from_list(0)
    #             pp = ProductPage(self.driver)
    #             title = pp.product_title()
    #             self.assertIn(product, title, "incorrect title")
    #             pp.add_to_cart()
    #             bp = BasketPage(self.driver)
    #             product_name = bp.check_product_name_in_cart()
    #             self.assertIn( product, product_name,"Selected product not added to basket")
    #             hp.return_to_home_page()
    #         else:
    #             hp.return_to_home_page()
    #
    # def test_remove_all_product_from_basket(self):
    # DZIALA
    #     """Test poprawnego dodania wielu produktów niezaleznie od rodzaju"""
    #     product_list = ["dsgdsgsgdfg","Frontend developer. Kurs video. HTML i CSS. Poziom średnio zaawansowany",
    #                     "Tysiąc szklanek herbaty. Spotkania na Jedwabnym Szlaku",
    #                     "English 4 IT. Praktyczny kurs języka angielskiego dla specjalistów IT i nie tylko"]
    #
    #     hp = HomePage(self.driver)
    #     sp = SearchPage(self.driver)
    #     pp = ProductPage(self.driver)
    #     bp = BasketPage(self.driver)
    #
    #     for product in product_list:
    #         hp.enter_searched_product(product)
    #         results = sp.search_results_is_not_empty()
    #         if results is True:
    #             sp.choose_product_from_list(0)
    #             pp = ProductPage(self.driver)
    #             title = pp.product_title()
    #             self.assertIn(product, title, "incorrect title")
    #             pp.add_to_cart()
    #             bp = BasketPage(self.driver)
    #             product_name = bp.check_product_name_in_cart()
    #             self.assertIn(product, product_name, "Selected product not added to basket")
    #             hp.return_to_home_page()
    #         else:
    #             hp.return_to_home_page()
    #
    #     hp.go_to_basket()
    #     bp.select_all_products()
    #     bp.click_remove_selected()
    #     bp.remove_results()

    def test_remove_selected_product_from_basket(self):
        """Test poprawnego usuniecia wybranych produktów z koszyka"""
        product_list = ["dsgdsgsgdfg", "Frontend developer. Kurs video. HTML i CSS. Poziom średnio zaawansowany",
                        "Tysiąc szklanek herbaty. Spotkania na Jedwabnym Szlaku",
                        "English 4 IT. Praktyczny kurs języka angielskiego dla specjalistów IT i nie tylko"]
        product_to_remove = ["Tysiąc szklanek herbaty. Spotkania na Jedwabnym Szlaku", "English 4 IT. Praktyczny kurs języka angielskiego dla specjalistów IT i nie tylko"]

        hp = HomePage(self.driver)
        sp = SearchPage(self.driver)
        pp = ProductPage(self.driver)
        bp = BasketPage(self.driver)

        for product in product_list:
            hp.enter_searched_product(product)
            results = sp.search_results_is_not_empty()
            if results is True:
                sp.choose_product_from_list(0)
                pp = ProductPage(self.driver)
                title = pp.product_title()
                self.assertIn(product, title, "incorrect title")
                pp.add_to_cart()
                bp = BasketPage(self.driver)
                product_name = bp.check_product_name_in_cart()
                self.assertIn(product, product_name, "Selected product not added to basket")
                hp.return_to_home_page()
            else:
                hp.return_to_home_page()

        hp.go_to_basket()
        for product in product_to_remove:
            print(f"to jest nazwa produktu ktory usuniemy {product}")
            bp.check_checkbox(product)

        bp.click_remove_selected()
        remove_results = bp.remove_results()
        print(f"to jest lista produktów ktore zostały w koszyku : {remove_results}")




if __name__=="__main__":
    unittest.main(verbosity=2)

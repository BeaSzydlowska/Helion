from Tests.baseTest import BaseTest
from Pages.homePage import HomePage
from Pages.basketPage import BasketPage
from Pages.searchPage import SearchPage
from Pages.productPage import ProductPage
import unittest
import csv
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
class BasketTest(BaseTest):
    #
    # def test_01_add_selected_book_to_basket_from_product_page_with_quantity(self):
    #     """Sprawdzenie możliwości dodania kilku sztuk tej samej ksiazki z karty produktu  do koszyka"""
    #     product = "Python dla każdego. Podstawy programowania. Wydanie III"
    #     quantity = 4
    #
    #     hp = HomePage(self.driver)
    #     hp.enter_searched_product(product)
    #     sp = SearchPage(self.driver)
    #     results = sp.search_results_is_not_empty()
    #     if results is True:
    #         sp.choose_product_from_list(0)
    #     pp = ProductPage(self.driver)
    #     title = pp.product_title()
    #     self.assertIn(product, title, "incorrect title")
    #     pp.enter_book_quantity(quantity)
    #     pp.add_to_cart()
    #     bp = BasketPage(self.driver)
    #     product_name = bp.check_product_name_in_cart()
    #     self.assertIn(product, product_name, "Selected product not added to basket")
    #     amount = bp.check_quantity_of_selected_product(product)
    #     self.assertEqual(quantity, amount, "incorrect amount of added product")


    @data(*get_data("Tests/titles.csv"))
    @unpack
    def test_02_add_multiple_product_to_basket(self, *products):

        """Test poprawnego dodania wielu produktów niezaleznie od rodzaju"""
        # product_list = ["Frontend developer. Kurs video. HTML i CSS. Poziom średnio zaawansowany", "fdsfdgfdgfdgdfg",
        #                 "Tysiąc szklanek herbaty. Spotkania na Jedwabnym Szlaku",
        #                 "English 4 IT. Praktyczny kurs języka angielskiego dla specjalistów IT i nie tylko"]

        hp = HomePage(self.driver)
        sp = SearchPage(self.driver)
        pp = ProductPage(self.driver)
        bp = BasketPage(self.driver)

        for product in products:
            hp.enter_searched_product(product)

            results = sp.search_results_is_not_empty()
            if results is True:
                default_sorting = sp.verify_if_sorting_by_best_match_is_set_as_default()
                self.assertTrue(default_sorting, "Sorting by best match is not set as default")
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
    #
    # def test_03_remove_all_product_from_basket(self):
    #     """Sprawdzenie możliwosci poprawnego usuniecia wszystkich produktów z koszyka (opróżnienia koszyka)"""
    #     product_list = ["Frontend developer. Kurs video. HTML i CSS. Poziom średnio zaawansowany", "fdsfdgfdgfdgdfg",
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
    #
    #         results = sp.search_results_is_not_empty()
    #         if results is True:
    #             default_sorting = sp.verify_if_sorting_by_best_match_is_set_as_default()
    #             self.assertTrue(default_sorting, "Sorting by best match is not set as default")
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
    #     info = bp.remove_results()
    #     self.assertEqual(info, "Twój koszyk jest pusty", "Your basket is not empty")
    #
    # def test_04_remove_selected_products_from_basket(self):
    #     """Sprawdzenie możliwosci poprawnego usuniecia wybranych produktów z koszyka"""
    #     product_list = ["dsgdsgsgdfg", "Frontend developer. Kurs video. HTML i CSS. Poziom średnio zaawansowany",
    #                     "Tysiąc szklanek herbaty. Spotkania na Jedwabnym Szlaku",
    #                     "English 4 IT. Praktyczny kurs języka angielskiego dla specjalistów IT i nie tylko"]
    #     product_to_remove = ["Tysiąc szklanek herbaty. Spotkania na Jedwabnym Szlaku",
    #                          "English 4 IT. Praktyczny kurs języka angielskiego dla specjalistów IT i nie tylko"]
    #     product_left = ["Frontend developer. Kurs video. HTML i CSS. Poziom średnio zaawansowany"]
    #
    #     hp = HomePage(self.driver)
    #     sp = SearchPage(self.driver)
    #     pp = ProductPage(self.driver)
    #     bp = BasketPage(self.driver)
    #
    #     for product in product_list:
    #         hp.enter_searched_product(product)
    #
    #         results = sp.search_results_is_not_empty()
    #         if results is True:
    #             default_sorting = sp.verify_if_sorting_by_best_match_is_set_as_default()
    #             self.assertTrue(default_sorting, "Sorting by best match is not set as default")
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
    #     hp.go_to_basket()
    #     for product in product_to_remove:
    #         print(f"to jest nazwa produktu ktory usuniemy {product}")
    #         bp.check_checkbox(product)
    #
    #     bp.click_remove_selected()
    #     remove_results = bp.remove_results()
    #     print(f"to jest lista produktów ktore zostały w koszyku : {remove_results}")
    #     self.assertEqual(remove_results, product_left, "Something went wrong, propably selected product was not removed")


if __name__ == "__main__":
    unittest.main(verbosity=2)

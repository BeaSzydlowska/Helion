from Tests.baseTest import BaseTest
from Pages.homePage import HomePage
from Pages.searchPage import SearchPage
from Pages.productPage import ProductPage
import unittest

class registerTest(BaseTest):
    def test_register_empty_fieds(self):
        """Test proby rejestracji przy  użyciu poprawnych danych """
        hp = HomePage(self.driver)
        hp.go_to_register_page()

    def test_register_empty_name_field(self):
        """Test proby rejestracji przy  przy pozostawionych wszystkich pustych polach"""

        pass

    def test_register_using_inorrect_email_format(self):
        """Test proby rejestracji przy uzyciu niepoprawnego emaila"""
        pass







if __name__=="__main__":
    unittest.main(verbosity=2)

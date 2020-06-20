from Tests.baseTest import BaseTest
from Pages.homePage import HomePage
from Pages.registerPage import RegisterPage
from Pages.accountPage import AccountPage
from Pages.loginPage import LoginPage
from Pages.searchPage import SearchPage
from Pages.productPage import ProductPage
import unittest

class loginTest(BaseTest):
    # def test_01_login__with_correct_data(self):
    #     """Sprawdzenie możliwości zalogowania użytkownika przy wpisaniu poprawnych(istniejących w systemie) danych."""
    #     mail = "hivoc67077@qmrbe.com"
    #     password = 'haslo12345'
    #     greeting = "Witaj"
    #     hp = HomePage(self.driver)
    #     hp.accept_cookie_policy()
    #     hp.go_to_login_page()
    #     lp = LoginPage(self.driver)
    #     lp.fill_email(mail)
    #     lp.fill_password(password)
    #     lp.click_on_login_btn()
    #     ap= AccountPage(self.driver)
    #     greeting_text = ap.verify_logged_in()
    #     self.assertEqual(greeting, greeting_text, "Something went wrong, probably you are not logged in")


    def test_02_login__with_incorrect_data(self):
        """Sprawdzenie możliwości zalogowania użytkownika na dane nieistniejące w serwisie"""
        mail = "sgsgfdhhh@gfgfdfgdf.ct"
        password = 'haslo12345'
        error = "Niestety podałeś niewłaściwy adres email lub hasło."
        hp = HomePage(self.driver)
        hp.accept_cookie_policy()
        hp.go_to_login_page()
        lp = LoginPage(self.driver)
        lp.fill_email(mail)
        lp.fill_password(password)
        lp.click_on_login_btn()
        errors = lp.visible_errors()
        self.assertEqual(error, errors, "Something went wrong, probably you are not logged in")


if __name__=="__main__":
    unittest.main(verbosity=2)
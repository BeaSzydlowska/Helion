from Tests.baseTest import BaseTest
from Pages.homePage import HomePage
from Pages.accountPage import AccountPage
from Pages.loginPage import LoginPage
import unittest


class LoginTest(BaseTest):

    def test_loginWithCorrectData(self):
        """Sprawdzenie możliwości zalogowania użytkownika przy wpisaniu poprawnych(istniejących w systemie) danych."""
        mail = "hivoc67077@qmrbe.com"
        password = 'haslo12345'
        greeting = "Witaj"
        hp = HomePage(self.driver)
        hp.accept_cookie_policy()
        hp.go_to_login_page()
        lp = LoginPage(self.driver)
        lp.fill_email(mail)
        lp.fill_password(password)
        lp.click_on_login_btn()
        ap = AccountPage(self.driver)
        greeting_text = ap.verify_logged_in()
        self.assertEqual(greeting, greeting_text, "Something went wrong, probably you are not logged in")

    def test_loginWithIncorrectData(self):
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
    unittest.main()
from Tests.baseTest import BaseTest
from Pages.homePage import HomePage
from Pages.accountPage import AccountPage
from Pages.loginPage import LoginPage
import unittest


class AccountTest(BaseTest):

    def test_correctlyLoggedOut(self):
        """checks the possibility to correctly log out from an account"""
        mail = "hivoc67077@qmrbe.com"
        password = 'haslo12345'
        greeting = "Witaj"
        message = "Zostałeś poprawnie wylogowany"
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
        ap.click_on_logout_btn()
        logout_message = lp.verify_logout()
        self.assertEqual(message, logout_message, "Something went wrong, probably you are not logged out")


if __name__=="__main__":
    unittest.main()
from Tests.baseTest import BaseTest
from Pages.homePage import HomePage
from Pages.registerPage import RegisterPage
from Pages.accountPage import AccountPage
import unittest


class RegisterTest(BaseTest):

    def test_registeCorrectData(self):
        """checks the possibility to register account if the required fields are filled with the correct data
        and required regulations are selected"""
        mail = "hivoc67077@qmrbe.com"
        password = 'haslo12345'
        activation_info = 'Aktywacja konta w helion.pl, sprawdź swój e-mail!'
        hp = HomePage(self.driver)
        hp.accept_cookie_policy()
        hp.go_to_register_page()
        rp = RegisterPage(self.driver)
        rp.fill_email(mail)
        rp.fill_password(password)
        rp.repeat_password(password)
        rp.check_regulation()
        rp.click_on_register_btn()
        ap= AccountPage(self.driver)
        activation = ap.verify_registration()
        self.assertEqual(activation, activation_info, "Something went wrong, probably your accont was not created")

    def test_registerAllfieldsAreEmpty(self):
        """checks the possibility to register account if the required fields are blank
        and required regulations are not selected"""

        errors = ["Podanie poprawnego emaila jest konieczne do dokończenia procesu rejestracji", "Wprowadź hasło (min. 5 znaków)", "Hasła muszą się zgadzać", "Musisz zaakceptować regulamin"]
        hp = HomePage(self.driver)
        hp.go_to_register_page()
        rp = RegisterPage(self.driver)
        rp.click_on_register_btn()
        visible_erros = rp.verify_visible_errors()
        for error in visible_erros:
            self.assertIn(error, errors, "Selected error-info not appeared")

    def test_registerUsingInorrectEmailFormat(self):
        """checks the possibility to register account if email field is filled with the incorrect data and required regulations are selected"""

        errors = ["Podanie poprawnego emaila jest konieczne do dokończenia procesu rejestracji"]
        password = 'haslo12345'
        hp = HomePage(self.driver)
        hp.go_to_register_page()
        rp = RegisterPage(self.driver)
        rp.fill_password(password)
        rp.repeat_password(password)
        rp.check_regulation()
        rp.click_on_register_btn()
        visible_erros =rp.verify_visible_errors()
        for error in visible_erros:
            self.assertIn(error, errors, "Selected error-info not appeared")


if __name__=="__main__":
    unittest.main()

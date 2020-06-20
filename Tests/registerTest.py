from Tests.baseTest import BaseTest
from Pages.homePage import HomePage
from Pages.registerPage import RegisterPage
from Pages.accountPage import AccountPage
from Pages.searchPage import SearchPage
from Pages.productPage import ProductPage
import unittest

class registerTest(BaseTest):
    # def test_register_password_and_confirm_password_are_different(self):
    #     """Test proby rejestracji przy  pozostawionym pustym polu  Powtórz hasło"""
    #     mail = "hivoc67077@qmrbe.com"
    #     password = 'haslo12345'
    #     activation_info = 'Aktywacja konta w helion.pl, sprawdź swój e-mail!'
    #     hp = HomePage(self.driver)
    #     hp.accept_cookie_policy()
    #     hp.go_to_register_page()
    #     rp = RegisterPage(self.driver)
    #     rp.fill_email(mail)
    #     rp.fill_password(password)
    #     rp.repeat_password(password)
    #     rp.check_regulation()
    #     rp.click_on_register_btn()
    #     ap= AccountPage(self.driver)
    #     activation = ap.verify_registration()
    #     self.assertEqual(activation, activation_info , "You are not ina correct page")



    # def test_register_all_fields_are_empty(self):
    #     # DZIALA
    #     """Test proby rejestracji przy  przy pozostawionych wszystkich pustych polach"""
    #     """Test proby rejestracji przy  użyciu poprawnych danych """
    #     errors = ["Podanie poprawnego emaila jest konieczne do dokończenia procesu rejestracji", "Wprowadź hasło (min. 5 znaków)", "Hasła muszą się zgadzać", "Musisz zaakceptować regulamin"]
    #
    #     hp = HomePage(self.driver)
    #     hp.go_to_register_page()
    #     rp = RegisterPage(self.driver)
    #     rp.click_on_register_btn()
    #     visible_erros =rp.verify_visible_errors()
    #     for error in visible_erros:
    #         self.assertIn(error, errors, "Nie pojawił sie komunikat o błędzie")

    # def test_register_using_inorrect_email_format(self):
    #     """Test proby rejestracji przy uzyciu niepoprawnego emaila"""
    #     #DZIALA
    #     errors = ["Podanie poprawnego emaila jest konieczne do dokończenia procesu rejestracji"]
    #     password = 'haslo12345'
    #     hp = HomePage(self.driver)
    #     hp.go_to_register_page()
    #     rp = RegisterPage(self.driver)
    #
    #     rp.fill_password(password)
    #     rp.repeat_password(password)
    #     rp.check_regulation()
    #     rp.click_on_register_btn()
    #     visible_erros =rp.verify_visible_errors()
    #     for error in visible_erros:
    #         self.assertIn(error, errors, "Nie pojawił sie komunikat o błędzie")
    #
    # def test_register_password_and_confirm_password_are_empty(self):
    #     # DZIALA
    #     """Test proby rejestracji przy  przy pozostawionych pustych polach Twoje hasło i Powtórz hasło"""
    #     errors = ["Wprowadź hasło (min. 5 znaków)", "Hasła muszą się zgadzać"]
    #     mail = "hivoc67077@qmrbe.com"
    #     hp = HomePage(self.driver)
    #     hp.go_to_register_page()
    #     rp = RegisterPage(self.driver)
    #     rp.fill_email(mail)
    #     rp.check_regulation()
    #     rp.click_on_register_btn()
    #     visible_erros = rp.verify_visible_errors()
    #     for error in visible_erros:
    #         self.assertIn(error, errors, "Nie pojawił sie komunikat o błędzie")
    #
    # def test_register_confirm_password_is_empty(self):
    #     # DZIALA
    #     """Test proby rejestracji przy  pozostawionym pustym polu  Powtórz hasło"""
    #     errors = ["Hasła muszą się zgadzać"]
    #     mail = "hivoc67077@qmrbe.com"
    #     password = 'haslo12345'
    #     hp = HomePage(self.driver)
    #     hp.go_to_register_page()
    #     rp = RegisterPage(self.driver)
    #     rp.fill_email(mail)
    #     rp.fill_password(password)
    #     rp.check_regulation()
    #     rp.click_on_register_btn()
    #     visible_erros = rp.verify_visible_errors()
    #     for error in visible_erros:
    #         self.assertIn(error, errors, "Nie pojawił sie komunikat o błędzie")

    def test_register_password_and_confirm_password_are_different(self):
        """Test proby rejestracji przy  pozostawionym pustym polu  Powtórz hasło"""
        errors = ["Hasła muszą się zgadzać"]
        mail = "hivoc67077@qmrbe.com"
        password = 'haslo12345'
        password_confirm = 'haslo1234'
        hp = HomePage(self.driver)
        hp.accept_cookie_policy()
        hp.go_to_register_page()
        rp = RegisterPage(self.driver)
        rp.fill_email(mail)
        rp.fill_password(password)
        rp.repeat_password(password_confirm)
        rp.check_regulation()
        rp.click_on_register_btn()
        visible_erros = rp.verify_visible_errors()
        for error in visible_erros:
            self.assertIn(error, errors, "Nie pojawił sie komunikat o błędzie")



    # def test_register_empty_name_field(self):
    #     """Test proby rejestracji przy  przy pozostawionych wszystkich pustych polach"""
    #
    #     pass
    #
    # def test_register_using_inorrect_email_format(self):
    #     """Test proby rejestracji przy uzyciu niepoprawnego emaila"""
    #     pass
    #
    #





if __name__=="__main__":
    unittest.main(verbosity=2)

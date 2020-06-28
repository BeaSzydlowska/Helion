from Pages.basePage import BasePage
from Locators.locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    def fill_email(self, email):
        """allows to enter an email"""
        mail = self.driver.find_element(*LoginPageLocators.EMAIL)
        mail.send_keys(email)

    def fill_password(self, password):
        """allows to enter a password"""
        passwd = self.driver.find_element(*LoginPageLocators.PASSWORD)
        passwd.send_keys(password)

    def click_on_login_btn(self):
        """allows to click on <<Zaloguj się>> button"""
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(LoginPageLocators.ZALOGUJ_BTN))
        self.driver.find_element(*LoginPageLocators.ZALOGUJ_BTN).click()

    def verify_logout(self):
        """returns "Zostałeś poprawnie wylogowany"string"""
        logout_message = self.driver.find_element(*LoginPageLocators.LOGOUT_MESSAGE)
        return logout_message.text

    def visible_errors(self):
        """returns displayed errors"""
        error = self.driver.find_element(*LoginPageLocators.ERROR)
        return error.text

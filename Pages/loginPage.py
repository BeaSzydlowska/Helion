from Pages.basePage import  BasePage
from Locators.locators import HomePageLocators
from Locators.locators import LoginPageLocators
from time import sleep

class LoginPage(BasePage):
    def fill_email(self,email):
        mail = self.driver.find_element(*LoginPageLocators.EMAIL)
        mail.send_keys(email)

    def fill_password(self, password):
        passwd = self.driver.find_element(*LoginPageLocators.PASSWORD)
        passwd.send_keys(password)

    def click_on_login_btn(self):
        self.driver.find_element(*LoginPageLocators.ZALOGUJ_BTN).click()

    def click_on_signup_btn(self):
        self.driver.find_element(*LoginPageLocators.SIGN_UP_BTN).click()


from Pages.basketPage import BasePage
from Locators.locators import RegisterPageLocators


class RegisterPage(BasePage):
    def fill_email(self, email):
        mail = self.driver.find_element(*RegisterPageLocators.EMAIL)
        mail.send_keys(email)

    def fill_password(self, password):
        passwd = self.driver.find_element(*RegisterPageLocators.PASSWORD)
        passwd.send_keys(password)

    def repeat_password(self, password):
        passwd = self.driver.find_element(*RegisterPageLocators.REPEAT_PASSWORD)
        passwd.send_keys(password)

    def check_regulation(self):
        self.driver.find_element(*RegisterPageLocators.REGULATIONS_CHECKBOX).click()

    def check_newsletter(self):
        self.driver.find_element(*RegisterPageLocators.REGISTER_BTN).click()

    def click_on_register_btn(self):
        self.driver.find_element(*RegisterPageLocators.REGISTER_BTN).click()
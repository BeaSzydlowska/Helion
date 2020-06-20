from Pages.basketPage import BasePage
from Locators.locators import RegisterPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(RegisterPageLocators.REGULATIONS_CHECKBOX))
        self.driver.find_element(*RegisterPageLocators.REGULATIONS_CHECKBOX).click()

    def check_newsletter(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(RegisterPageLocators.NEWSLETTER_CHECKBOX))
        self.driver.find_element(*RegisterPageLocators.NEWSLETTER_CHECKBOX).click()

    def click_on_register_btn(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(RegisterPageLocators.REGISTER_BTN))
        self.driver.find_element(*RegisterPageLocators.REGISTER_BTN).click()

    def verify_visible_errors(self):
        errors = self.driver.find_elements(*RegisterPageLocators.ERRORS)
        visible_errors = []
        for error in errors:
            if error.is_displayed():
                error = error.text
                visible_errors.append(error)
        return visible_errors


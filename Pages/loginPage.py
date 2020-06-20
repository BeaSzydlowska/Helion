from Pages.basePage import  BasePage
from Locators.locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def fill_email(self,email):
        mail = self.driver.find_element(*LoginPageLocators.EMAIL)
        mail.send_keys(email)

    def fill_password(self, password):
        passwd = self.driver.find_element(*LoginPageLocators.PASSWORD)
        passwd.send_keys(password)

    def click_on_login_btn(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(LoginPageLocators.ZALOGUJ_BTN))
        self.driver.find_element(*LoginPageLocators.ZALOGUJ_BTN).click()


    def visible_errors(self):
        error = self.driver.find_element(*LoginPageLocators.ERROR)
        return error.text
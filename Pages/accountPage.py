from Pages.basketPage import BasePage
from Locators.locators import AccountPageLocators
from time import sleep

class AccountPage(BasePage):
    def verify_registration(self):
        activation_info = self.driver.find_element(*AccountPageLocators.TEXT_CONFIRMATION)
        return activation_info.text

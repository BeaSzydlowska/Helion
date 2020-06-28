from selenium import webdriver
from Pages.basketPage import BasePage
from Locators.locators import HomePageLocators
from Locators.locators import AccountPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountPage(BasePage):

    def verify_registration(self):
        """allows to check if register confirmation text appear after register"""
        activation_info = self.driver.find_element(*AccountPageLocators.TEXT_CONFIRMATION)
        return activation_info.text

    def verify_logged_in(self):
        """allows to check if greeting appeared after login to account"""
        greeting = self.driver.find_element(*AccountPageLocators.GREETING)
        return greeting.text

    def click_on_logout_btn(self):
        """allows to click <Wyloguj się> button"""
        account_btn = self.driver.find_element(*HomePageLocators.ACCOUNT_BTN)
        webdriver.ActionChains(self.driver).move_to_element(account_btn).perform()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(AccountPageLocators.LOG_OUT_BTN))
        self.driver.find_element(*AccountPageLocators.LOG_OUT_BTN).click()

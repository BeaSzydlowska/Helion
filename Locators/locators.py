from selenium.webdriver.common.by import By
class HomePageLocators():
    SEARCHER = (By.ID, "inputSearch")
    SEARCH_BTN = (By.XPATH,"//button[@class='button']")
    BASKET_COUNTER = (By.ID, "koszykbox")
    GO_TO_BASKET = (By.XPATH, "//span[@class='hideFixed']")
    ACCOUNT_BTN = (By.XPATH, "//div[@class='your-profile']//a[contains(text(),'Twoje konto')]")
    LOGIN_BTN = (By.CLASS_NAME, "login-link")
    REGISTER_BTN = (By.CLASS_NAME, "register-link")
    COOKIE = (By.ID, "rodo-ok")


class LoginPageLocators():
    EMAIL= (By.NAME, "loginemail")
    PASSWORD = (By.NAME, "haslo")
    ZALOGUJ_BTN = (By.XPATH, "//button[contains(text(),'Zaloguj się')]")
    SIGN_UP_BTN =(By.XPATH, "//a[@class='button']")
    ERROR = (By.XPATH, "//h4[contains(text(),'Niestety podałeś niewłaściwy adres email lub hasło.')]")

class RegisterPageLocators():
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "haslo1")
    REPEAT_PASSWORD = (By.NAME, "haslo2")
    REGULATIONS_CHECKBOX = (By.XPATH, "//label[@for='zgoda']")
    NEWSLETTER_CHECKBOX = (By.XPATH, "//label[@for='newsletter_tak']")
    REGISTER_BTN = (By.XPATH, "//button[contains(text(),'Zakładam konto')]")
    ERRORS = (By.XPATH, "//div[@class='error-info']/p/label[@class='error']")


class AccountPageLocators():
    TEXT_CONFIRMATION = (By.XPATH,"//p[contains(text(),'Aktywacja konta w helion.pl, sprawd')]")
    GREETING = (By.XPATH, "//a[@id='helloUser']")

class SearchPageLocators():
    LIST_OF_SEARCHED_PRODUCTS = (By.XPATH, "//ul[@class='list']/li")
    # LIST_OF_SEARCHED_PRODUCTS = (By.XPATH, "//ul[@class='list']/li//img")
    LIST_OF_NAMES = (By.XPATH, "//ul[@class='list']/li//h3/a")
    ADD_TO_CART_BTN = (By.XPATH, "//p[contains(@class, 'price-incart')]/a[@rel='nofollow']")
    NO_SEARCH_RESULTS = (By.CLASS_NAME, "not-found")

class ProductPageLocators():
    TITLE = (By.XPATH, "//h1/span[@itemprop ='name']")
    BOOK_QUANTITY = (By.CLASS_NAME, "amount-button")
    ADD_BOOK_TO_BASKET = (By.ID, "addToBasket_pytdk3")
    ADD_EBOOK_TO_BASKET = (By.ID, "addToBasket_pytdk3_ebook")
    BOOK_BOX = (By.ID, "box_druk")
    EBOOK_BOX = (By.ID, "box_ebook")
    ADD_TO_CART_BTN_LIST = (By.XPATH, "//a[contains(text(), 'Dodaj do koszyka')]")
    BOX = (By.XPATH, "//fieldset[@class='active']")
    ADD_TO_CART = (By.XPATH, "//fieldset[@class='active']/p[2]/a[contains(text(), 'Dodaj do koszyka')]")


class BasketPageLocators():
    ROWS = (By.XPATH, "//table[@id='koszyk']/tbody/tr[@class='pozycja']")
    AMOUNT = (By.XPATH, "//table[@id='koszyk']/tbody/tr[@class='pozycja']/td[@class='amount']//input[@class = 'ilosc']")
    TITLE = (By.XPATH, "//table[@id='koszyk']/tbody/tr[@class='pozycja']//td[@class='desc']//a")
    REMOVE = (By.XPATH, "//a[contains(text(),'zaznaczone')]")
    BACK = (By.CLASS_NAME, "more")
    SELECT_ALL = (By.XPATH, "//th[@class='checkbox']//span[@class='input']")
    EMPTY_BASKET = (By.XPATH, "//p[contains(text(),'Twój koszyk jest pusty')]")





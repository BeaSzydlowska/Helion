from selenium.webdriver.common.by import By
class HomePageLocators():
    SEARCHER = (By.ID, "inputSearch")
    SEARCH_BTN = (By.XPATH,"//button[@class='button']")
    BASKET_COUNTER = (By.ID, "koszykbox")
#     Python dla każdego. Podstawy programowania. Wydanie III Michael Dawson

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



class CartPageLocators():
    ROWS = (By.XPATH, "//table[@id='koszyk']/tbody/tr[@class='pozycja']")
    REMOVE = (By.XPATH, "//a[contains(text(),'zaznaczone')]")


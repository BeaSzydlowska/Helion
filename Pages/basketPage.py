from Pages.basePage import  BasePage
from Locators.locators import BasketPageLocators
from time import sleep


class BasketPage(BasePage):
    def check_product_name_in_cart(self):
        rows = self.driver.find_elements(*BasketPageLocators.ROWS)
        for row in rows:
            name = row.find_element_by_xpath("//td[@class='desc']//h2/a")
            print(name.text)
            return name.text
            sleep(10)


    def check_quantity_of_selected_product(self, product):
        rows = self.driver.find_elements(*BasketPageLocators.ROWS)
        for row in rows:
            name = row.find_element_by_xpath("//td[@class='desc']//h2/a")

            if name.text in product:
                amount = row.find_element_by_xpath("//td[@class='amount']//input[@class = 'ilosc']")
                amount = amount.get_attribute("value")
                print(amount)
            return int(amount)


    def check_checkbox(self, product):
        rows = self.driver.find_elements(*BasketPageLocators.ROWS)

        for row in rows:
            name = row.find_element_by_xpath("td[@class='desc']//h2/a")
            print(f"to jest name.text{name.text}")
            # if name.text in product:
            if product in name.text:
                print("weszlo w ifa")
                checkbox = row.find_element_by_xpath("td/div/label/span[@class='input']")
                checkbox.click()
                sleep(5)
                i = False
                if checkbox.is_selected():
                    i = True
                else:
                    i = False
                print(i)










    def click_remove_selected(self):
        remove_btn = self.driver.find_element(*BasketPageLocators.REMOVE)
        remove_btn.click()
        sleep(5)
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()
        sleep(5)



    def remove_results(self):
        try:
            napis = self.driver.find_element(*BasketPageLocators.EMPTY_BASKET)
            print(napis.text)
            return napis.text

        except:
            list_of_products = []
            rows = self.driver.find_elements(*BasketPageLocators.ROWS)
            for row in rows:
                name = row.find_element_by_xpath("//td[@class='desc']//h2/a")
                print(name.text)
                list_of_products.append(name.text)
                print(list_of_products)
                return list_of_products




    def select_all_products(self):
        select_all_btn = self.driver.find_element(*BasketPageLocators.SELECT_ALL)
        select_all_btn.click()
        rows = self.driver.find_elements(*BasketPageLocators.ROWS)
        i = False
        for row in rows:
            checkbox = row.find_element_by_xpath("td/div/input[@type = 'checkbox']")
            if checkbox.is_selected():
                i = True
            else:
                i = False
            print(i)





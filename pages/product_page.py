from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        button.click()

    def name_product_current_add_product(self):
        current_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        add_product = self.browser.find_element(*ProductPageLocators.NAME_ADD_PRODUCT).text
        assert current_product == add_product, "Different names products"

    def price_basket_current_price_product(self):
        price_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        print(price_basket)
        price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        print(price_product)
        assert price_product in price_basket, "Different price product and basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_ADD_PRODUCT), \
            "Success message is presented, but should not be"

    def disappeared_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_ADD_PRODUCT), \
            "Success message is presented, but should not be"

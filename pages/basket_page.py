#Ожидаем, что в корзине нет товаров
#Ожидаем, что есть текст о том что корзина пуста
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), \
            "Success empty_basket"
    def text_basket_empty_present(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET), \
            "Success empty_basket"
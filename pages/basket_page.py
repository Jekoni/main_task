from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Basket is not empty"
    
    def should_be_basket_empty_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "Item in basket"
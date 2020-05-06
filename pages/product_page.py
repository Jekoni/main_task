from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class PageObject(BasePage):

    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Button is not presented"
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()
		
    def should_be_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        basket_name = self.browser.find_element(*ProductPageLocators.BASKET_NAME).text
        assert book_name == basket_name, "Name is different"
       
    def should_be_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert book_price == basket_price, "Price is different"
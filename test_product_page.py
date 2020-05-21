from .pages.product_page import PageObject
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest

@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage(): 
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        time.sleep(2)
        self.login_page.register_new_user(email, password)
        time.sleep(2)
        self.login_page.should_be_authorized_user() 
        time.sleep(2)
		
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        self.product_page = PageObject(browser, link)
        self.product_page.open()
        self.product_page.add_to_basket()
        self.product_page.should_be_book_name()
        self.product_page.should_be_book_price()
        time.sleep(2)
	
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.product_page = PageObject(browser, link)
        self.product_page.open()
        #self.product_page.add_to_basket()
        self.product_page.should_not_be_success_message()
        time.sleep(2)

		
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_book_name()
    product_page.should_be_book_price()
    time.sleep(2)
	
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()
    time.sleep(2)
	
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()
    time.sleep(2)

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.element_disappeared()
    time.sleep(2)
	
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.should_be_login_link()
	
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.go_to_login_page()
	
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.should_be_basket_empty_message()
    time.sleep(2)	

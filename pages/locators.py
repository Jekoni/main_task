from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
class LoginPageLocators():
    LOGIN_URL= (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM= (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
	
    REGISTER_FORM= (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#registration-password2")
	
class  ProductPageLocators():
    ADD_BUTTON= (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME= (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE= (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    BASKET_NAME = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    BASKET_PRICE= (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")
	
class BasePageLocators ():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
   

class BasketPageLocators ():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    EMPTY_BASKET = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
	

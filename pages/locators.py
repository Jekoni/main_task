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
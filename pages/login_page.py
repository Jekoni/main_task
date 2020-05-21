from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_link.click()
        assert "login" in self.browser.current_url, "There is not login in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"
	
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        password1_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password1_field.send_keys(password)
        password2_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        password2_field.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_button.click()
		
	
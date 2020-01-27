from .base_page import BasePage
from .locators import LoginPageLocators
import selenium

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #current_url = self.current_url
        assert "login" in self.browser.current_url, "Not found login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def register_new_user(self, email, password):
        registration_email = self.browser.find_element (*LoginPageLocators.REGISTRATION_EMAIL)
        registration_email.send_keys(email)
        registration_password = self.browser.find_element (*LoginPageLocators.REGISTRATION_PASSWORD)
        registration_password.send_keys(password)
        registration_password_repeat = self.browser.find_element (*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT)
        registration_password_repeat.send_keys(password)
        button_registration = self.browser.find_element (*LoginPageLocators.BUTTON_REGISTRATION)
        button_registration.click()

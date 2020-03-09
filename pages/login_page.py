from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, "Url for login page doesn't contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN_FORM is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "REGISTER_FORM is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        check_password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_CHECK_FIELD)
        check_password_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

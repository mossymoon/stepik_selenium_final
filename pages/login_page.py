from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "url is wrong"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_USER_NAME), "No login form user name"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_USER_EMAIL), "No login form user e-mail"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_USER_EMAIL), "Wrong e-mail"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_USER_PASS), "Wrong password"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_USER_REPASS), "Wrong re-password"

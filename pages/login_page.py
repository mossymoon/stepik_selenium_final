from .base_page import BasePage
from .locators import LoginPageLocators
import faker

class LoginPage(BasePage):

    def should_be_login_page(self):
        # проверка перехода на страницу login
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "url is wrong"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_USER_NAME), "No login form user name"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_USER_EMAIL), "No login form user e-mail"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_USER_EMAIL), "Wrong e-mail"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_USER_PASS), "Wrong password"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_USER_REPASS), "Wrong re-password"

    def register_new_user(self):
        # проверка регистрации нового юзера
        self.register_data_login_pass()
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_register.click()

    def register_data_login_pass(self):
        # ввод данных e-mail, password для регистрации
        f = faker.Faker()
        email = f.email()
        email_register = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_USER_EMAIL)
        email_register.send_keys(email)
        password = "EveryBody3434%^&*"
        password_register = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_USER_PASS)
        password_register.send_keys(password)
        re_password_register = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_USER_REPASS)
        re_password_register.send_keys(password)

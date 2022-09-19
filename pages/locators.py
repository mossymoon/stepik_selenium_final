from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM_USER_NAME = (By.XPATH, '//*[@id="id_login-username"]')
    LOGIN_FORM_USER_EMAIL = (By.XPATH, '//*[@id="id_login-password"]')
    REGISTER_FORM_USER_EMAIL = (By.XPATH, '//*[@id="id_registration-email"]')
    REGISTER_FORM_USER_PASS = (By.XPATH, '//*[@id="id_registration-password1"]')
    REGISTER_FORM_USER_REPASS = (By.XPATH, '//*[@id="id_registration-password2"]')

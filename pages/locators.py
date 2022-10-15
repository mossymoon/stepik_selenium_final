from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM_USER_NAME = (By.XPATH, '//*[@id="id_login-username"]')
    LOGIN_FORM_USER_EMAIL = (By.XPATH, '//*[@id="id_login-password"]')
    REGISTER_FORM_USER_EMAIL = (By.XPATH, '//*[@id="id_registration-email"]')
    REGISTER_FORM_USER_PASS = (By.XPATH, '//*[@id="id_registration-password1"]')
    REGISTER_FORM_USER_REPASS = (By.XPATH, '//*[@id="id_registration-password2"]')

class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    PRODUCT_CHECK = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_CHECK2 = (By.XPATH, '//*[@id="messages"]/div[1]/div')
    PRODUCT_CHECK3 = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRICE_CHECK = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]')
    PRICE_CHECK2 = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    PRICE_CHECK3 = (By.CSS_SELECTOR, "#messages strong")
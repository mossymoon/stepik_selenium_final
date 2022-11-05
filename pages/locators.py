from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM_USER_NAME = (By.XPATH, '//*[@id="id_login-username"]')
    LOGIN_FORM_USER_EMAIL = (By.XPATH, '//*[@id="id_login-password"]')
    REGISTER_FORM_USER_EMAIL = (By.XPATH, '//*[@id="id_registration-email"]')
    REGISTER_FORM_USER_PASS = (By.XPATH, '//*[@id="id_registration-password1"]')
    REGISTER_FORM_USER_REPASS = (By.XPATH, '//*[@id="id_registration-password2"]')
    BUTTON_REGISTER = (By.XPATH, '//button[@name="registration_submit"]')

class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, '//*[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_CHECK = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_CHECK2 = (By.XPATH, '//*[@id="messages"]/div[1]/div')
    PRODUCT_CHECK3 = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRICE_CHECK = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]')
    PRICE_CHECK2 = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    PRICE_CHECK3 = (By.CSS_SELECTOR, "#messages strong")
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div')
    BASKET_BUTTON = (By.XPATH, './/a[contains(@href,"/en-gb/basket")][contains(text(),"View basket")]')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_MAIN_PAGE = (By.XPATH, './/a[@class="btn btn-default"]')
    BASKET_HAS_NO_GOODS = (By.XPATH, '//*[@id="content_inner"]/p')
    BASKET_NOT_EMPTY = (By.XPATH, '//*[@id="messages"]/div[1]/div/text()')

import time

from .base_page import BasePage
from .locators import MainPageLocators, BasketPageLocators
from .login_page import LoginPage
from .locators import ProductPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def go_to_product_page(self):
        product_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        product_basket.click()

    def should_not_be_success_message(self):
        not_success_alert = self.browser.is_not_element_present(*ProductPageLocators.PRODUCT_CHECK2)
        return not_success_alert()

    def click_basket_button(self):
        basket_button = self.browser.find_element(*BasketPageLocators.BASKET_MAIN_PAGE)
        basket_button.click()

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)



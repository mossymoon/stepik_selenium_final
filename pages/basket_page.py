import time

from .base_page import BasePage
from .locators import MainPageLocators, BasketPageLocators
from .login_page import LoginPage
from .locators import ProductPageLocators


class BasketPage(BasePage):

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), \
            "The basket is not empty, but should be empty"

    def basket_should_not_have_goods(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_HAS_NO_GOODS), \
            "The basket should not have goods, but it has"
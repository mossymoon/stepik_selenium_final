from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_is_empty(self):
    # проверка что корзина пуста
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), \
            "The basket is not empty, but should be empty"

    def click_basket_button(self):
    # нажатие на кнопку корзины
        basket_button = self.browser.find_element(*BasketPageLocators.BASKET_MAIN_PAGE)
        basket_button.click()

    def basket_should_not_have_goods(self):
    # проверка что в корзине нет добавленных товаров
        assert self.is_element_present(*BasketPageLocators.BASKET_HAS_NO_GOODS), \
            "The basket should not have any goods, but it has"

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def check_correct_name(self):
        # проверка совпадения названий добавленного продукта в корзину
        check_name = self.browser.find_element(*ProductPageLocators.PRODUCT_CHECK)
        check_name2 = self.browser.find_element(*ProductPageLocators.PRODUCT_CHECK2)
        check_name3 = self.browser.find_element(*ProductPageLocators.PRODUCT_CHECK3)
        assert check_name2.text == f"{check_name.text} has been added to your basket.", "Product is not added to the basket"
        assert check_name.text == check_name3.text, "Both texts are exist"

    def add_to_basket_on_product_page(self):
        # добавление продукта в корзину
        product_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        product_basket.click()

    def check_correct_price(self):
        # проверка совпадения цены добавленного продукта
        check_price2 = self.browser.find_element(*ProductPageLocators.PRICE_CHECK2)
        check_price3 = self.browser.find_elements(*ProductPageLocators.PRICE_CHECK3)[2]
        assert check_price2.get_attribute("innerText") == check_price3.get_attribute("innerText"), "Price is not equal"

    def should_not_be_success_message(self):
        # проверка отсутсвия успешного сообщения
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should_not_be_success_message"

    def should_see_as_disappearing_message(self):
        # проверка исчезновения успешного сообщения
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but it should disappear"

    def click_basket_button(self):
        # нажатие на кнопку "Посмотреть корзину"
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

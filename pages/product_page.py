from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import MainPageLocators
from .login_page import LoginPage

class ProductPage(BasePage):

    def check_correct_name(self):
        check_name = self.browser.find_element(*ProductPageLocators.PRODUCT_CHECK)
        check_name2 = self.browser.find_element(*ProductPageLocators.PRODUCT_CHECK2)
        check_name3 = self.browser.find_element(*ProductPageLocators.PRODUCT_CHECK3)
        assert check_name2.text == f"{check_name.text} был добавлен в вашу корзину.", "Product is not added to the basket"
        assert check_name.text == check_name3.text, "Both texts are exist"

    def check_correct_price(self):
        check_price2 = self.browser.find_element(*ProductPageLocators.PRICE_CHECK2)
        check_price3 = self.browser.find_elements(*ProductPageLocators.PRICE_CHECK3)[2]
        assert check_price2.get_attribute("innerText") == check_price3.get_attribute("innerText"), "Price is not equal"
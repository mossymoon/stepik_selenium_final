import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = MainPage(browser, link)
    page2 = ProductPage(browser, link)
    page.open()
    page2.add_to_basket_on_product_page()
    page.solve_quiz_and_get_code()
    page2.check_correct_name()
    page2.check_correct_price()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page2 = ProductPage(browser, link)
    page.open()
    page2.add_to_basket_on_product_page()
    page2.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page2 = ProductPage(browser, link)
    page.open()
    page2.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page2 = ProductPage(browser, link)
    page.open()
    page2.add_to_basket_on_product_page()
    page2.should_see_as_disappearing_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click_basket_button()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_not_have_goods()
    basket_page.basket_is_empty()

@pytest.mark.register_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link_login = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page_login = LoginPage(browser, link_login)
        page_login.open()
        page_login.register_new_user()
        page_login.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link_product = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link_product)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = MainPage(browser, link)
        page2 = ProductPage(browser, link)
        page2.open()
        page2.add_to_basket_on_product_page()
        page.solve_quiz_and_get_code()
        page2.check_correct_name()
        page2.check_correct_price()

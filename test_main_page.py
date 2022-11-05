import pytest
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.click_basket_button()
    basket_page.basket_should_not_have_goods()
    basket_page.basket_is_empty()

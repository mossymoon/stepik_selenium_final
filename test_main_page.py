from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    login = LoginPage(browser, url)
    page.open()  # открываем страницу
    page.go_to_login_page()  # переход на страницу логина
    page.should_be_login_link()  # проверка наличия ссылки на логин
    login.should_be_login_url()  # проверка наличия правильного url
    login.should_be_login_form()  # проверка наличия формы авторизации
    login.should_be_register_form()  # проверка наличия формы регистрации

def go_to_login_page(self, browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

from .pages.login_page import LoginPage


def test_guest_should_see_login_page_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_should_be_find_login_form_in_page(browser):
    url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_form()

def test_should_be_find_register_form_in_page(browser):
    url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, url)
    page.open()
    page.should_be_register_form()
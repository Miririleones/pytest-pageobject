from selenium.webdriver.common.by import By
import time

link = "https://vk.com/"


def go_to_login_page(browser):
    url = browser.current_url

    print(url)
    # login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    # login_link.click()

def base_page_is_a_not_current_page(browser, base_page_title):
    assert browser.title != base_page_title, f"Твоя страница БАЗОВАЯ"

def base_page_is_a_current_page(browser, base_page_title):
    assert browser.title == base_page_title, f"Ты перешел НЕ НА {base_page_title}, а вот сюда {browser.title}"

def get_page_title(browser, page_url):
    browser.get(page_url)

    return browser.title

def print_page_title(title):

    print(title)

def test_guest_can_go_to_login_page(browser):

    base_page_title = get_page_title(browser, "https://vk.com/")

    print_page_title(base_page_title)

    new_page_title = get_page_title(browser, "https://yandex.kz/")

    print_page_title(new_page_title)

    browser.back()

    time.sleep(5)

    base_page_is_a_current_page(browser, base_page_title)

    browser.refresh()

    print_page_title(browser.title)

    browser.back()

    base_page_is_a_not_current_page(browser, base_page_title)
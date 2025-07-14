from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.should_be_promo_url()
    page.should_be_to_basket_button()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_product_name()
    page.should_be_product_cost()
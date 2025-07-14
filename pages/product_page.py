from selenium.common.exceptions import NoAlertPresentException
from pages.base_page import BasePage
from pages.locators import ProductPageLocators
import math


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.is_element_present(*ProductPageLocators.PRODUCT_CARD_NAME)
        self.is_element_present(*ProductPageLocators.PRODUCT_CARD_COST)

        self.PRODUCT_NAME = self.browser.find_element(*ProductPageLocators.PRODUCT_CARD_NAME).text
        self.PRODUCT_COST = self.browser.find_element(*ProductPageLocators.PRODUCT_CARD_COST).text

    def should_be_promo_url(self):
        self.is_url_element_present(ProductPageLocators.PROMO_NEWYEAR_PATH_PARAMS)

    def should_be_to_basket_button(self):
        self.is_element_present(*ProductPageLocators.BUTTON_FOR_ADD_TO_BASKET)

    def click_add_to_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_FOR_ADD_TO_BASKET)
        basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_product_name(self):
        self.is_element_present(*ProductPageLocators.ALERT_SUCCESS_NAME)

        alert_success_name = self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS_NAME).text

        assert self.PRODUCT_NAME in alert_success_name, f"Incorrect product added: expected {self.PRODUCT_NAME}, got {alert_success_name}"

    def should_be_product_cost(self):
        self.is_element_present(*ProductPageLocators.ALERT_INFO_COST)

        alert_info_cost = self.browser.find_element(*ProductPageLocators.ALERT_INFO_COST).text

        assert self.PRODUCT_COST == alert_info_cost, f"Product cost: expected {self.PRODUCT_COST}, got {alert_info_cost}"
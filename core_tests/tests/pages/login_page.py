from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.PAGE_URL in self.browser.current_url, f"This is not a {LoginPageLocators.PAGE_URL} page."

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM)
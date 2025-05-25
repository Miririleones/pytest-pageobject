from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    PAGE_URL = "notlogin"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    PRODUCT_CARD_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_CARD_COST = (By.CSS_SELECTOR, ".price_color")
    ALERT_INFO_COST = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")
    ALERT_SUCCESS_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong:first-child")
    PROMO_NEWYEAR_PATH_PARAMS = "?promo=newYear"
    BUTTON_FOR_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
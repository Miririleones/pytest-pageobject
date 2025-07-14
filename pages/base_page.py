from selenium.common.exceptions import TimeoutException


class BasePage():
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): 
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except(TimeoutException):
            return False
        return True
    
    def is_url_element_present(self, what):
        try:
            assert what in self.browser.current_url, f"{what} element in url not found"
        except(TimeoutException):
            return False
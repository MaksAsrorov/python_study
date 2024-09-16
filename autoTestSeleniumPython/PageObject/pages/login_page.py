from study.autoTestSeleniumPython.PageObject.pages.base_page import BasePage
# from study.autoTestSeleniumPython.PageObject.pages.base_page import url
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        # self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form, "Login form is not exist"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        registration_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM)
        assert registration_form, "Login form is not exist"
        assert True

    def should_be_login_url(self):
       url = self.browser.driver.current_url
    # реализуйте проверку на корректный url адрес
       assert "login" in url, "Нет логина"
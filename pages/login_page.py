from selenium.common import TimeoutException
from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

def fake_user_data():
    login=str(time.time())+'@fake.ru'
    password='Votetodaa'+str(time.time())
    return login,password

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.url

    def should_be_login_form(self):
        assert WebDriverWait(self.browser, 7).until(ec.presence_of_element_located(LoginPageLocators.LOGIN_FORM))

    def should_be_register_form(self):
        assert WebDriverWait(self.browser,7).until(ec.presence_of_element_located(LoginPageLocators.REGISTER_FORM))

    def register_new_user(self):
        self.new_user = fake_user_data()
        self.email = self.new_user[0]
        self.password = self.new_user[1]
        btn_login=WebDriverWait(self.browser,7).until((ec.element_to_be_clickable(LoginPageLocators.LOGIN_LINK)))
        btn_login.click()
        reg_form=WebDriverWait(self.browser, 7).until(ec.presence_of_element_located(LoginPageLocators.REGISTER_FORM))
        reg_form.find_element(*LoginPageLocators.REG_EMAIL).send_keys(self.email)
        reg_form.find_element(*LoginPageLocators.REG_PASSWORD1).send_keys(self.password)
        reg_form.find_element(*LoginPageLocators.REG_PASSWORD2).send_keys(self.password)
        WebDriverWait(self.browser,7).until(ec.element_to_be_clickable(LoginPageLocators.REG_BTN)).click()
        try:
            WebDriverWait(self.browser,7).until(ec.visibility_of_element_located(LoginPageLocators.REG_ALERT_SUCCESS))
            assert True
        except TimeoutException:
            raise AssertionError("Message about successful registration wasn't found")

from selenium.webdriver.common.by import By


class BasketPageLocators():
    ITEMS_CONTAINER=(By.CSS_SELECTOR,'.content .row')
    EMPTY_BASKET_MESSAGE=(By.CSS_SELECTOR,'#content_inner p')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    GO_TO_CART = (By.CSS_SELECTOR, '.btn-group>a[href*="basket"]')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_LINK=(By.CSS_SELECTOR,'#login_link')
    LOGIN_FORM=(By.CSS_SELECTOR,'#login_form')
    REGISTER_FORM=(By.CSS_SELECTOR,'div .register_form')
    REG_EMAIL=(By.CSS_SELECTOR,'#id_registration-email')
    REG_PASSWORD1=(By.CSS_SELECTOR,'#id_registration-password1')
    REG_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BTN=(By.CSS_SELECTOR, 'button[name="registration_submit"]')
    REG_ALERT_SUCCESS=(By.CSS_SELECTOR, '.alert-success')
class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_TITLE=(By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE=(By.CSS_SELECTOR,'.product_main>.price_color')
    ADDED_TITLE=(By.CSS_SELECTOR, '#messages strong')
    ADDED_PRICE=(By.CSS_SELECTOR, '.alert-info strong')
    SUCCES_ALERT=(By.CSS_SELECTOR,'#messages>.alert-success:nth-of-type(1)')
from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class ProductPage(BasePage):
    def add_item_into_cart(self):
        self.title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        self.price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        add_btn=WebDriverWait(self.browser,7).until(ec.element_to_be_clickable(ProductPageLocators.ADD_TO_CART))
        add_btn.click()
        self.solve_quiz_and_get_code()

    def check_title(self):
        added_title=WebDriverWait(self.browser,7).until(ec.visibility_of_element_located(ProductPageLocators.ADDED_TITLE))
        assert self.title==added_title.text, f"Title is {self.title} should be equal to {added_title.text}"

    def check_price(self):
        added_price=WebDriverWait(self.browser,7).until(ec.visibility_of_element_located(ProductPageLocators.ADDED_PRICE))
        assert self.price==added_price.text, f"Price is {self.price} should be equal to {added_price.text}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCES_ALERT), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCES_ALERT)




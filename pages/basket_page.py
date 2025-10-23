from pages.base_page import BasePage
from pages.locators import BasketPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasketPage(BasePage):

    def should_be_message_empty_basket(self):
        actual_text=WebDriverWait(self.browser,7).until(ec.presence_of_element_located(BasketPageLocators.EMPTY_BASKET_MESSAGE)).text
        assert 'Your basket is empty' in actual_text, f'actual text is: "{actual_text}"'

    def should_not_have_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_CONTAINER)

    def should_be_url(self):
        assert 'basket' in self.url

    def should_be_added_item(self):
        assert WebDriverWait(self.browser,7).until(ec.presence_of_element_located())
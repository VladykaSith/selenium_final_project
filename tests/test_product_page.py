from pyexpat.errors import messages

from pages.base_page import BasePage
from pages.product_page import ProductPage
def test_user_can_add_item_into_cart(browser):
    link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page=ProductPage(browser,link)
    page.open()
    page.add_item_into_cart()
    page.check_title()
    page.check_price()


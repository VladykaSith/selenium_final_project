from pages.product_page import ProductPage
import pytest
links=["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
@pytest.mark.parametrize('link', links[0:2])
def test_user_can_add_item_into_cart(browser,link):

    page=ProductPage(browser,link)
    page.open()
    page.add_item_into_cart()
    page.check_title()
    page.check_price()

@pytest.mark.xfail(reason="Must fail by default")
@pytest.mark.parametrize('link', links[0:2])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_into_cart()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', links[0:2])
def test_guest_cant_see_success_message(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Must fail by default")
@pytest.mark.parametrize('link', links[0:2])
def test_message_disappeared_after_adding_product_to_basket(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_into_cart()
    page.should_disappear()




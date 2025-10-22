from selenium.webdriver.common.by import By

def test(browser):
    browser.get('https://selenium1py.pythonanywhere.com/ru/basket/')
    message=browser.find_element(By.CSS_SELECTOR,'#content_inner p').text
    print(message)
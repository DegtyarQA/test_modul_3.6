from selenium.webdriver.common.by import By
import time


def test_items(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    #slovo = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    #x = slovo.text
    #assert "Añadir al carrito" == x

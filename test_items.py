from selenium.webdriver.common.by import By
import time

link = ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")


def test_find_button_busket(browser):
    browser.get(link)
    time.sleep(30)
    x = len(browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"))
    assert x >0, "Alarm, button is not found!!!"


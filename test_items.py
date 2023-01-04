from selenium.webdriver.common.by import By
import time

link = ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")


def test_items(browser):
    browser.get(link)
    time.sleep(10)
    x = len(browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"))
    assert x >0 , "Alarm!!!"


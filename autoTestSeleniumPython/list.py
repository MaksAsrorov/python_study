from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math


def calc(x, y):
    return int(x) + int(y)

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.ID, "num1")
    x = num1_element.text


    num2_element = browser.find_element(By.ID, "num2")
    y = num2_element.text

    z = calc(x, y)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(z))

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()

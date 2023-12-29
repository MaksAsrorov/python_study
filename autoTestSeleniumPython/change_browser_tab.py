from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_click = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    first_click.click()

    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input_result = browser.find_element(By.ID, "answer")
    input_result.send_keys(y)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()

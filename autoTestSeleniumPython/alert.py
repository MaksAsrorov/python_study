from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_click = browser.find_element(By.TAG_NAME, "button")
    first_click.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input_result = browser.find_element(By.ID, "answer")
    input_result.send_keys(y)

    # confirm = browser.switch_to.alert
    # confirm.accept()
    # confirm.dissmiss()

    # prompt = browser.switch_to.alert
    # prompt.send_keys("My answer")
    # prompt.accept()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()

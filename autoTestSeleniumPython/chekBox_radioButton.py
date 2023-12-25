from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input_result = browser.find_element(By.XPATH, "//input[@id='answer']")
    input_result.send_keys(y)

    click_checkBox = browser.find_element(By.XPATH, "//label[@for='robotCheckbox']")
    click_checkBox.click()

    click_radiobutton = browser.find_element(By.XPATH, "//label[@for='robotsRule']")
    click_radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

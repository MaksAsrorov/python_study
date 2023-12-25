from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# people_checked = people_radio.get_attribute("checked")
# print("value of people radio: ", people_checked)
# assert people_checked is not None, "People radio is not selected by default"


try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    box = browser.find_element(By.ID, "treasure")

    x_element = box.get_attribute("valuex")
    x = x_element
    y = calc(x)

    input_result = browser.find_element(By.ID, "answer")
    input_result.send_keys(y)

    click_checkBox = browser.find_element(By.ID, "robotCheckbox")
    click_checkBox.click()

    click_radiobutton = browser.find_element(By.ID, "robotsRule")
    click_radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

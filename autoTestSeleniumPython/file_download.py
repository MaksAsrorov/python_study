from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)



    #

    #
    # x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    # x = x_element.text
    # y = calc(x)

    input_result = browser.find_element(By.NAME, "firstname")
    input_result.send_keys("Макс")

    input_result = browser.find_element(By.NAME, "lastname")
    input_result.send_keys("Асроров")

    input_result = browser.find_element(By.NAME, "email")
    input_result.send_keys("test@yandex.ru")



    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys("C:/ProjectX/test.txt")

    submit_button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()

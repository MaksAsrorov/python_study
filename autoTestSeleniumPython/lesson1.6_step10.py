from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    input_first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first") # XPath: //div[@class="first_block"]/div/input[@class="form-control first"]
    input_first_name.send_keys("Ivan")

    input_last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
    input_last_name.send_keys("Petrov")

    input_email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
    input_email.send_keys("1@1.ru")

    submit_button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    submit_button.click()

    success_text_element = browser.find_element(By.TAG_NAME, "h1")

    assert "Congratulations! You have successfully registered!" == success_text_element.text # сравниваем текст в лейбле результата с ожидаемым

finally:
    time.sleep(10)
    browser.quit()


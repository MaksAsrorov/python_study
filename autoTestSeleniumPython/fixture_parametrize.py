import unittest
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import math

from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('page', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
# @pytest.mark.parametrize('page', ["236899"])
def test_guest_should_see_login_link1(browser, page):
    link = f"https://stepik.org/lesson/{page}/step/1"
    browser.get(link)

    browser.implicitly_wait(10)
    input1 = browser.find_element(By.XPATH, "//a[@id='ember33']")
    input1.click()

    input2 = browser.find_element(By.XPATH, "//input[@id='id_login_email']")
    input2.send_keys("maksim.asrorov@gmail.com")

    input3 = browser.find_element(By.XPATH, "//input[@id='id_login_password']")
    input3.send_keys("M1234567890")

    input4 = browser.find_element(By.XPATH, "//button[@type='submit']")
    input4.click()


    input8 = browser.find_element(By.XPATH, "//button[text()='Решить снова']")
    input8.click()


@pytest.mark.parametrize('page', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
# @pytest.mark.parametrize('page', ["236899"])
def test_guest_should_see_login_link(browser, page):
    link = f"https://stepik.org/lesson/{page}/step/1"
    browser.get(link)

    browser.implicitly_wait(10)
    input1 = browser.find_element(By.XPATH, "//a[@id='ember33']")
    input1.click()

    input2 = browser.find_element(By.XPATH, "//input[@id='id_login_email']")
    input2.send_keys("maksim.asrorov@gmail.com")

    input3 = browser.find_element(By.XPATH, "//input[@id='id_login_password']")
    input3.send_keys("M1234567890")

    input4 = browser.find_element(By.XPATH, "//button[@type='submit']")
    input4.click()

    time.sleep(1)
    input6 = browser.find_element(By.XPATH, "//textarea")
    input6.send_keys(math.log(int(time.time())))
    input7 = browser.find_element(By.XPATH, "//button[text()='Отправить']")
    input7.click()
    #
    browser.implicitly_wait(2)
    answer_block = browser.find_element(By.XPATH, "//div[starts-with(@class, 'smart-hints')]")
    element_text = answer_block.text
    print(element_text, "sdafakjshdfkjhaskldjfhaksjdhfkjasdhkjfashdkfjh")

    browser.implicitly_wait(2)
    input8 = browser.find_element(By.XPATH, "//button[text()='Решить снова']")
    input8.click()

    browser.implicitly_wait(2)
    assert element_text == 'Correct!', f"expected {element_text}, got {answer_block}"




if __name__ == "__main__":
    unittest.main()

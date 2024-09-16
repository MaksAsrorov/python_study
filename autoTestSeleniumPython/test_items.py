from selenium.webdriver.common.by import By

def test_guest_should_see_login_link_pass(browser, language):
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser, language):
    browser.find_element(By.CSS_SELECTOR, "#magic_link")
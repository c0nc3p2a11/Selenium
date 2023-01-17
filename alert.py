"""selecting alert,
    acceptation of alert"""
import time
from math import sin, log
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
LINK = 'http://suninjuly.github.io/alert_accept.html'


def res(number_element):
    """calculating"""
    result = log(abs(12 * sin(int(number_element.text))))
    return result

try:
    driver.get(LINK)
    driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    alert = driver.switch_to.alert
    alert.accept()

    number = driver.find_element(By.ID, 'input_value')
    answer_field = driver.find_element(By.ID, 'answer')
    answer_field.send_keys(res(number))
    btn = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    btn.click()
finally:
    time.sleep(10)
    driver.quit()

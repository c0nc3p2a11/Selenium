import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
LINK = 'http://suninjuly.github.io/explicit_wait2.html'

def res(number_element):
    """calculating"""
    result = log(abs(12 * sin(int(number_element.text))))
    return result

try:
    driver.get('http://suninjuly.github.io/explicit_wait2.html')

    # по методам EC https://selenium-python.readthedocs.io/waits.html
    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = driver.find_element(By.ID, 'book').click()
    # решение старой задачи
    number = driver.find_element(By.ID, 'input_value')
    answer_field = driver.find_element(By.ID, 'answer')
    answer_field.send_keys(res(number))
    btn = driver.find_element(By.ID, 'solve')
    btn.click()
finally:
    time.sleep(5)
    driver.quit()

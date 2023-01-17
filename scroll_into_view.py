import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from math import sin,log


browser = webdriver.Chrome()
res = lambda x: log(abs(12*sin(int(x.text))))

try:
    browser.get('https://suninjuly.github.io/execute_script.html')

    x = browser.find_element(By.ID, 'input_value')
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(res(x))
    radio = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', radio)
    radio.click()
    browser.find_element(By.ID, 'robotCheckbox').click()
    btn = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)

    btn.click()
    time.sleep(3)
finally:
    browser.quit()

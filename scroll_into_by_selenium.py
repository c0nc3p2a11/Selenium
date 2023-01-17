from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    res = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    res.location_once_scrolled_into_view # переход на кнопку посредством селениума
    res.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # закрываем браузер после всех манипуляций
    time.sleep(3)
    browser.quit()


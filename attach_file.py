'''Attaching file '''
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# получаем путь к директории текущего исполняемого
# Так делается для того чтобы путь был не до окружения

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

# добавляем к этому пути имя файла
FILE_PATH = os.path.join(CURRENT_DIR, 'file_name_here.txt')
LINK = 'http://suninjuly.github.io/file_input.html'

try:
    driver = webdriver.Chrome()
    driver.get(LINK)
    first_name = driver.find_element(By.NAME, 'firstname')
    first_name.send_keys('Oleg')
    last_name = driver.find_element(By.NAME, 'lastname')
    last_name.send_keys('kiselev')
    email = driver.find_element(By.NAME, 'email')
    email.send_keys('test@test.com')
    attach = driver.find_element(By.ID, 'file')
    attach.send_keys(FILE_PATH)
    driver.find_element(By.XPATH, '/html/body/div/form/button').click()
finally:
    time.sleep(5)
    driver.quit()

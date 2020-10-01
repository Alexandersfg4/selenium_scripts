from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PATH = '/Users/aleksandrbortnikov/Documents/WebDrivers/chromedriver' #path to the driver
driver = webdriver.Chrome(PATH)
driver.get('https://www.w3schools.com/')

link = driver.find_element_by_link_text("Learn Python")
link.click()

#find elemnts on page until they will be presented or time is ended (10 sec)
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.LINK_TEXT,'Start learning Python now »')))
    link = driver.find_element_by_link_text("Start learning Python now »")
    link.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.LINK_TEXT,'Next ❯')))
    link = driver.find_element_by_link_text("Next ❯")
    link.click()
    #show previous page
    driver.back()
except Exception as exc:
    print(f'{exc}')
    sleep(3)
    driver.quit()

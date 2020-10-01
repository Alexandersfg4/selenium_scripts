from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
PATH = '/Users/aleksandrbortnikov/Documents/WebDrivers/chromedriver' #path to the driver
driver = webdriver.Chrome(PATH)
driver.get('https://www.google.com')
print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "span")))
except Exception:
    driver.quit()

main = driver.find_elements_by_tag_name('span')
for words in main:
    print(words.text)
driver.quit() #exit from whole browser

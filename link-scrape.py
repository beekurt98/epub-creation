from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "URL"
driver = webdriver.Chrome()

driver.get(URL)
time.sleep(3)

paragraph_list = driver.find_elements(By.CSS_SELECTOR, value="div p")

file = open("links.txt", "a")

for p in paragraph_list:
    print(p)
    file.write(p.text)

file.close()
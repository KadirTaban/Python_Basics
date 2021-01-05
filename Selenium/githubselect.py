from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome("/home/mountainlabs/Documents/chromedriver")
url="https://github.com/KadirTaban"
driver.get(url)

searchInput = driver.find_element_by_name("q")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
result = driver.find_element_by_css_selector()
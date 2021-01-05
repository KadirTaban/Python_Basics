from selenium import webdriver
import datetime
a=webdriver.Chrome("/home/mountainlabs/Documents/chromedriver")

url="https://github.com/KadirTaban"
a.get(url)

a.maximize_window()
a.save_screenshot("kt.png")
print(a.title)

if "KadirTaban" in a.title:
    a.save_screenshot("kt1.png")
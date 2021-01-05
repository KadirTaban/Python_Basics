from instagramuserinfo import username, password, loginUsername
from selenium import webdriver
import time
class Instagram:
    def __init__(self,username,password,loginUsername):
        self.browser = webdriver.Chrome("/home/mountainlabs/Documents/chromedriver")
        self.username = username
        self.password=password
        self.loginUsername=loginUsername
    def signIn(self):
        self.browser.get("https://www.instagram.com")
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.loginUsername)
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
        time.sleep(5)
    def getFollow(self):
        self.browser.get(f"https://www.instagram.com/{username}/followers")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/ul/li[2]/a").click()
        dialog = self.browser.find_element_by_css_selector("div[role=dialog]")
        dialog_1=dialog.find_elements_by_css_selector("div[class=_1XyCr]")
        dialog_2=dialog_1.find_element_by_css_selector("ul[class=jjbaz_6xe7A]")
        followerCount=len(dialog.find_elements_by_css_selector("li"))
        print(f"first count:{followerCount} ")
        followers = dialog_2.find_elements_by_css_selector("li")
        for user in followers:
            link = user.find_elements_by_css_selector("a").get_attribute("href")
            print(link)
instagram=Instagram(username,password,loginUsername)
instagram.signIn()
instagram.getFollow()
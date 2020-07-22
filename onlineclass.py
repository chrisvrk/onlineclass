from selenium import webdriver
from time import sleep
from secrets import username, email

class   onlineclass():
    def __init__(self):
        self.driver = webdriver.Chrome('onlineclass/chromedriver.exe')
    def login(self):
        self.driver.get('https://meetingsemea25.webex.com/webappng/sites/meetingsemea25/meeting/download/259c9850d7063d16c30931447d4baa86') 
        sleep(5) 

        join_from_browser = self.driver.find_element_by_xpath('//*[@id="push_download_join_by_browser"]')
        join_from_browser.click()
    

        email_in = self.driver.find_element_by_xpath('//*[@id="meetingSimpleContainer"]/div[2]/div[2]/input')
        email_in.send_keys(username)























































bot = onlineclass()
bot.login()         



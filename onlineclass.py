from selenium import webdriver
from time import sleep
from secrets import username, email
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from teachers import glossa, maths , relegion, aoth, aepp, history, english 


opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })




class   onlineclass():
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options=opt, executable_path=r'D:\TOOLS-ISO-PROGGRAMING\project\onlineclass\chromedriver.exe')
    def login(self):
        self.driver.get(glossa) 
        sleep(5) 

        join_from_browser = self.driver.find_element_by_xpath('//*[@id="push_download_join_by_browser"]')
        join_from_browser.click()
        sleep(5)
        
        self.driver.switch_to.frame('pbui_iframe')
        username_in = self.driver.find_element_by_xpath('//*[@id="meetingSimpleContainer"]/div[2]/div[2]/input')
        username_in.send_keys(username)

        email_in = self.driver.find_element_by_xpath('//*[@id="meetingSimpleContainer"]/div[2]/div[3]/input')
        email_in.send_keys(email)

        join_meeting = self.driver.find_element_by_xpath('//*[@id="guest_next-btn"]')
        join_meeting.click()
        sleep(3)
        sleep(5)
    def mute(self):
        mute = self.driver.find_element_by_xpath('//*[@id="meetingSimpleContainer"]/div[3]/div[2]/div[1]/div/button')
        mute.click()
    def video(self):
        video = self.driver.find_element_by_xpath('//*[@id="meetingSimpleContainer"]/div[3]/div[2]/div[2]/div/button')
        video.click()    
    def join(self):
        join = self.driver.find_element_by_xpath('//*[@id="interstitial_join_btn"]')
        join.click()
bot = onlineclass()
bot.login()         
bot.mute()
bot.video()
bot.join()


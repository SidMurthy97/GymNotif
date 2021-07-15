from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from selenium.webdriver.common.keys import Keys

def auto_log_in():

    p_browser.find_element_by_id("onetrust-accept-btn-handler").click() #accept cookies

    username = p_browser.find_element_by_id('login-email') #type email
    username.send_keys(os.environ['gymuser'])

    pssword = p_browser.find_element_by_id('pin') #type pin
    pssword.send_keys(os.environ['gympass'])

    pssword = p_browser.find_element_by_id('pin').send_keys(Keys.RETURN) #press enter to log in


url = 'https://www.thegymgroup.com/member-area/my-gym/average-usage-chart/' #url of the usage chart

p_browser = webdriver.Chrome("C:\\Users\\murth\\Documents\\Projects\\Programming\\GymNotif\\chromedriver_win32\\chromedriver.exe") #change path to chromedriver based on your own machine
p_browser.get(url) #open new chrome instance 

time.sleep(1) #wait a second to let the page load, otherwise everything breaks

auto_log_in()


print("ended")
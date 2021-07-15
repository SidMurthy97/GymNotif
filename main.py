from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
import os
import time


def auto_log_in():

    p_browser.find_element_by_id("onetrust-accept-btn-handler").click() #accept cookies

    username = p_browser.find_element_by_id('login-email') #type email
    username.send_keys(os.environ['gymuser'])

    pssword = p_browser.find_element_by_id('pin') #type pin
    pssword.send_keys(os.environ['gympass'])

    pssword = p_browser.find_element_by_id('pin').send_keys(Keys.RETURN) #press enter to log in

def get_occupancy():

    Soup = soup(p_browser.page_source,"html.parser") #get relevant html code
    raw_capacity = (Soup.find("div",{"class":"circle lower animate"}))
    capacity_str = str(raw_capacity)
    index = capacity_str.find("%")

    print(capacity_str)
    capacity = capacity_str[index - 2] + capacity_str[index - 1]

    # print(index,capacity)
    return capacity




url = 'https://www.thegymgroup.com/member-area/my-gym/average-usage-chart/' #url of the usage chart

p_browser = webdriver.Chrome("C:\\Users\\murth\\Documents\\Projects\\Programming\\GymNotif\\chromedriver_win32\\chromedriver.exe") #change path to chromedriver based on your own machine
p_browser.get(url) #open new chrome instance 

time.sleep(3) #wait a second to let the page load, otherwise everything breaks

auto_log_in()

time.sleep(5) #wait some time to let the next page load

occupancy = get_occupancy()

print("Gym Occupancy is:",occupancy, "%")
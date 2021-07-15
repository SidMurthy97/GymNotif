from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://www.thegymgroup.com/member-area/my-gym/average-usage-chart/'
#initialise browser credentials for panopto
p_browser = webdriver.Chrome("C:\\Users\\murth\\Documents\\Projects\\Programming\\GymNotif\\chromedriver_win32\\chromedriver.exe") #change path to chromedriver based on your own machine
p_browser.get(url)
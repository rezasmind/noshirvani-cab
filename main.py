from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path='/home/daddy/chromedriver')

# Navigate to page

sleep(2)
driver.maximize_window()
sleep(2)
driver.get('http://elearning1.nit.ac.ir/') 
print(driver.title)
sleep(12)
username = driver.find_element(By.ID,"username")
password = driver.find_element(By.ID,"password")

username.send_keys("username")
password.send_keys("password")
password.send_keys(Keys.RETURN)

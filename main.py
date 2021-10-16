from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
from dotenv import load_dotenv , find_dotenv


load_dotenv(find_dotenv())

KALAMEKARBARI = os.getenv('KALAMEKARBARI')
RAMZ = os.getenv('RAMZ')





driver = webdriver.Chrome(executable_path='./chromedriver.exe')

# Navigate to page

sleep(2)
driver.maximize_window()
sleep(2)
driver.get('http://elearning1.nit.ac.ir/') 
print(driver.title)
sleep(12)

username = driver.find_element(By.ID,"username")
password = driver.find_element(By.ID,"password")

username.send_keys(KALAMEKARBARI)
password.send_keys(RAMZ)
password.send_keys(Keys.RETURN)

sleep(7)
cab = driver.find_element(By.CLASS_NAME,"fa-sign-in")
cab.click()

sleep(7)

print(driver.title)

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

sleep(20)
ActionChains(driver).send_keys(Keys.RETURN).perform()
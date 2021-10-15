from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path='/home/daddy/chromedriver')

# Navigate to page

sleep(2)
driver.maximize_window()
sleep(2)
driver.get('http://elearning1.nit.ac.ir/') 
print(driver.title)
sleep(5)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
from dotenv import load_dotenv , find_dotenv
import csv
import time


load_dotenv(find_dotenv())

KALAMEKARBARI = os.getenv('KALAMEKARBARI')
RAMZ = os.getenv('RAMZ')

if(os.path.exists("./hour.csv") == False):
    def hourdata():
        with open('hour.csv', 'w') as csvfile:
            w = csv.writer(csvfile,quoting=csv.QUOTE_NONE,escapechar=' ')
            save = "y"
            while save == "y":
                shanbe = list(map(str,input("(shanbe) saeat kelas haton ro ezafe konid (besorat => 16:00 , 13:00,...): ").split(" "))) 
                yekshan = list(map(str,input("(Yek shanbe) saeat kelas haton ro ezafe konid (besorat => 16:00 , 13:00,...): ").split(" ")))  
                doshan = list(map(str,input("(Do shanbe) saeat kelas haton ro ezafe konid (besorat => 16:00 , 13:00,...): ").split(" ")))  
                seshan = list(map(str,input("(Se shanbe) saeat kelas haton ro ezafe konid (besorat => 16:00 , 13:00,...): ").split(" ")))   
                chaharshan = list(map(str,input("(Chahar shanbe) saeat kelas haton ro ezafe konid (besorat => 16:00 , 13:00,...): ").split(" ")))  
                times = (shanbe,yekshan,doshan,seshan,chaharshan)
                save = input("mikhaid saeat haie vared shode ro zakhire konid? Y/N: ")  
                if save.lower() == "y":
                    for row in times:
                        w.writerow(row)
                    print("---saeat haie vared shode zakhire shode---")
                save = input("mikhaid dobare vared konid?? Y/N: ")
            print("etmam zakhire sazi data.")
    hourdata()



def attendClass():
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

    sleep(5400)
    driver.quit()
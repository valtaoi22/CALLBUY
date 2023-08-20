#Selenium imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from gtts import gTTS
import os
from os import path

from time import sleep
import time

def main():
     
    driver = webdriver.Chrome()
    driver.maximize_window()  

    driver.get('https://www.flipkart.com')

    time.sleep(10)

    cross = driver.find_element(By.XPATH,  '/html/body/div[2]/div/div/button').click()

    searchBar=driver.find_element( By.XPATH,  '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
    file1 = open('response_from_recording.txt' ,"r")
    searchBar.send_keys(file1.read())
    searchButton=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button').click()

    a = driver.current_url
    print(str(a))

    with open('response.txt', 'w',encoding='utf-8') as f:
            f.write("This is the link for Best reccomendations for you " + str(a))

            

if __name__=="__main__":
    main()


#time.sleep(5000)

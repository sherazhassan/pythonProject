import time

import pyautogui as pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
driver.get("http://haier.peopleqlik.pk/")

driver.find_element(By.ID,"txtEmail").send_keys("1")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(1) #needs to check if this works without time
driver.find_element(By.ID,"txtPassword").send_keys("123456")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(2)

driver.find_element(By.XPATH,"//*[@id='layout']/div[3]/a").click() #click on the main menu button
driver.find_element(By.XPATH,"//*[@id='mainMenu']/ul/li[1]/a").click() #click on the organization button
driver.find_element(By.XPATH,"//*[@id='mainMenu']/ul/li[1]/ul/li[7]/a").click() #click on the security button
driver.find_element(By.XPATH,"//*[@id='mainMenu']/ul/li[1]/ul/li[7]/ul/li[1]/a[1]").click() #click on the user screen
time.sleep(1)

driver.find_element(By.ID,"btnAdd").click() #clicking on the add button
time.sleep(1)

#Giving Inputs
a=driver.find_element(By.ID,"select2-ddlCompanyCode-container").click()
pyautogui.press("Haier Pakistan")
time.sleep(1)
#a.send_keys("haier") #selecting company

driver.find_element(By.ID,"txtEmailID").send_keys("c@c.com") #giving Email input
driver.find_element(By.ID,"select2-ddlRole-container").send_keys("ess") #assigning roles

driver.find_element(By.ID,"btnsubmit").click() #clicking to save record


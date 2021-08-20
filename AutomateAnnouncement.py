import time

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
driver.find_element(By.XPATH,"//*[@id='mainMenu']/ul/li[1]/a").click() #click on the organization module
driver.find_element(By.XPATH,"//*[@id='mainMenu']/ul/li[1]/ul/li[1]/a[1]").click() #click on the announcement screen
time.sleep(2)

driver.find_element(By.ID,"btnAdd").click()
driver.find_element(By.ID,"txtTitle").send_keys("testing automation check")
driver.find_element(By.ID,"btnsubmit").click()


import time
from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")

#driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://haier.peopleqlik.pk/")
driver.get("https://app.peopleqlik.com/")

driver.find_element(By.ID,"txtEmail").send_keys("tassawar.younas@bilytica.com.au")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(3)
driver.find_element(By.ID,"txtPassword").send_keys("123456")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='layout']/div[3]/a").click() #click on the main menu button
driver.find_element(By.XPATH,"//*[@id='mainMenu']/ul/li[2]/a").click() #click on the employee master module
driver.find_element(By.XPATH,"//*[@id='mainMenu']/ul/li[2]/ul/li[1]/a[1]").click() #click on the employee screen
time.sleep(5)

driver.find_element(By.XPATH,"//*[@id='dt_tableTools']/tbody/tr[1]/td[9]/div/div/div[1]/i").click() #click action menu

driver.find_element(By.XPATH,"//*[@id='e_8732312_001']").click() #click edit button
time.sleep(5)


#driver.close()
#driver.find_element(By.XPATH,"//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[1]/div/div[1]").click()
#time.sleep(5)
#b= select( driver.find_element_by_xpath("//*[@id='app-layer-location-field-leg1-origin-ta-dialog']/div[2]/div/div[1]/section"))

#b.send_keys("Lahore (LHE - Allam Iqbal Intl.)")

#time.sleep(3)
#a=driver.find_element(By.XPATH,"//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[1]/div/div[2]/div/div/div/button[1]").click()
#a.send_keys("Karachi (KHI - Jinnah Intl.)")
#driver.find_element(By.ID,"d1-btn").clear()
#driver.find_element(By.ID,"d1-btn").send_keys("Aug 4")
#driver.find_element(By.ID,"d2-btn").clear()
#driver.find_element(By.ID,"d2-btn").send_keys("Aug 20")

#driver.find_element(By.XPATH,"//*[@id='wizard-flight-pwa-1']/div[3]/div[2]").click()



import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#driver = webdriver.Chrome("D:\webdriver\chromedriver.exe")
#driver.get(url="https://app.peopleqlik.com/")
#driver.close()

driver=webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")

driver.get(url="https://app.peopleqlik.com/Home/Index")

print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("//*[@id='login_form']/form/div[3]/p/a[1]").click()

time.sleep(2)

driver.close()

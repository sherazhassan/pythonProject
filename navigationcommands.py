import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")

driver.get("https://stackoverflow.com/questions")
print(driver.title)

driver.get("https://geteasyqa.com/qa/best-test-case-templates-examples/")
print(driver.title)

driver.back()
time.sleep(2)
print(driver.title)

driver.forward()
time.sleep(2)
print(driver.title)

driver.close()
#driver.find_element_by_xpath("//*[@id='btnLogin]'")


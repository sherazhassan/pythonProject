import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")

driver.get("https://app.peopleqlik.com/")

user_ele=driver.find_element_by_name("login_username4")
print(user_ele.is_displayed())
print(user_ele.is_enabled())

user_ele.send_keys("tassawar.younas@bilytica.com.au")
driver.find_element_by_id("btnLogin").click()

#driver.get("https://app.peopleqlik.com/?ReturnUrl=/Home/index")

#frame=driver.find_element_by_xpath("//*[@id='txtPassword']")
#driver.switch_to.frame(frame)

time.sleep(2)
pwd_ele=driver.find_element_by_id("txtPassword")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

pwd_ele.send_keys("123456")
driver.find_element_by_id("btnLogin").click()

time.sleep(2)

driver.get("https://app.peopleqlik.com/?ReturnUrl=/Home/index")

cal_ele=driver.find_element_by_id("LiCalendar")
print("Status for the Calendar screen button is",cal_ele.is_selected())


hom_ele=driver.find_element_by_id("LiCalendar")
print("Status for the home screen button is",hom_ele.is_selected())


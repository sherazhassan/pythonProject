import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#For Super Admin Role
driver=webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
driver.get("http://haier.peopleqlik.pk/")
driver.find_element(By.ID,"txtEmail").send_keys("1")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(1)
driver.find_element(By.ID,"txtPassword").send_keys("123456")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(2)
#driver.find_element(By.XPATH,"//*[@id='layout']/div[3]/a").click() #click on the main menu button
#driver.find_element(By.ID,"userlogo").click() #click on user logo button
#driver.find_element(By.XPATH,"//*[@id='header_main']/div[1]/nav/div/ul/li[4]/div/ul/li[4]/a").click() #click on logout button

driver.find_element(By.XPATH,"//*[@id='layout']/div[3]/a").click() #click on the main menu button
#clicking on the Organization module > Announcement Screen
driver.find_element(By.XPATH, "//*[@id='mainMenu']/ul/li[1]/a").click()
adm_url_announcement = driver.get("http://haier.peopleqlik.pk/admin/Announcement")
time.sleep(3)

driver.find_element(By.XPATH,"//*[@id='layout']/div[3]/a").click() #click on the main menu button
#clicking on the Employee Master module > Employee Screen
driver.find_element(By.XPATH, "//*[@id='mainMenu']/ul/li[2]/a").click()
adm_url_employee = driver.get("http://haier.peopleqlik.pk/IA/Employee")
time.sleep(3)

driver.find_element(By.XPATH,"//*[@id='layout']/div[3]/a").click() #click on the main menu button
#clicking on the Payroll module > Process Payroll Screen
driver.find_element(By.XPATH, "//*[@id='mainMenu']/ul/li[3]/a").click()
adm_url_processpayroll = driver.get("http://haier.peopleqlik.pk/CP/ProcessPayroll")
time.sleep(3)

driver.find_element(By.XPATH,"//*[@id='layout']/div[3]/a").click() #click on the main menu button
#clicking on the Leave Tracker module > Leave Application  Screen
driver.find_element(By.XPATH, "//*[@id='mainMenu']/ul/li[4]/a").click()
adm_url_leave = driver.get("http://haier.peopleqlik.pk/LA/LeaveApplication")
time.sleep(3)

driver.find_element(By.XPATH,"//*[@id='layout']/div[3]/a").click() #click on the main menu button
#clicking on the Attendance module > Time Entry Screen
driver.find_element(By.XPATH, "//*[@id='mainMenu']/ul/li[5]/a").click()
adm_url_timeentry = driver.get("http://haier.peopleqlik.pk/LA/TimeEntry")
time.sleep(3)

driver.find_element(By.XPATH,"//*[@id='layout']/div[3]/a").click() #click on the main menu button
#clicking on the Self Service module > Time Off Screen
driver.find_element(By.XPATH, "//*[@id='mainMenu']/ul/li[6]/a").click()
adm_url_timeoff = driver.get("http://haier.peopleqlik.pk/ESS/LeaveRequest")
time.sleep(3)

driver.find_element(By.XPATH,"//*[@id='layout']/div[3]/a").click() #click on the main menu button
#clicking on the Integration module > Time Device Screen
driver.find_element(By.XPATH, "//*[@id='mainMenu']/ul/li[7]/a").click()
adm_url_timedevice = driver.get("http://haier.peopleqlik.pk/LA/Integration")
time.sleep(3)

driver.find_element(By.XPATH,"//*[@id='layout']/div[3]/a").click() #click on the main menu button
#clicking on the Reports module > General Reports Screen
driver.find_element(By.XPATH, "//*[@id='mainMenu']/ul/li[8]/a").click()
adm_url_genreports = driver.get("http://haier.peopleqlik.pk/Report/GeneralReport")
time.sleep(3)

driver.find_element(By.XPATH,"//*[@id='layout']/div[3]/a").click() #click on the main menu button
#clicking on the Analytics module > Payroll Summary Screen
driver.find_element(By.XPATH, "//*[@id='mainMenu']/ul/li[9]/a").click()
adm_url_paysum = driver.get("http://haier.peopleqlik.pk/AL/Payroll")
time.sleep(5)

driver.quit()

#For Self Service Role
driver=webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
driver.get("http://haier.peopleqlik.pk/")
driver.find_element(By.ID,"txtEmail").send_keys("a@a.com")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(1)
driver.find_element(By.ID,"txtPassword").send_keys("123456")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='layout']/div[3]/a").click() #click on the main menu button
#driver.find_element(By.ID,"userlogo").click() #click on user logo button
#driver.find_element(By.XPATH,"//*[@id='header_main']/div[1]/nav/div/ul/li[4]/div/ul/li[4]/a").click() #click on logout button

driver.find_element(By.XPATH, "//*[@id='mainMenu']/ul/li[1]/a").click() #ESS in a@a user
a_url_ess = driver.get("http://haier.peopleqlik.pk/ESS/LeaveRequest")

def are_urls_the_same(temp_url1,temp_url2):
    url_compare = ( == )

if are_urls_the_same()


#For Time Device Admin
driver=webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
driver.get("http://haier.peopleqlik.pk/")
driver.find_element(By.ID,"txtEmail").send_keys("b@b.com")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(1)
driver.find_element(By.ID,"txtPassword").send_keys("123456")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='layout']/div[3]/a").click() #click on the main menu button
#driver.find_element(By.ID,"userlogo").click() #click on user logo button
#driver.find_element(By.XPATH,"//*[@id='header_main']/div[1]/nav/div/ul/li[4]/div/ul/li[4]/a").click() #click on logout button
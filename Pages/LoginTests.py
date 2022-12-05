
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from login import Login
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

#when we must import a class in a file
# when we want to use a object the have all value of class.

#we must to pass driver argoamn for class attrebiute to use our driver
#ابجکت لاگین رو از روی کلاس لاگین ساخیم
login_object = Login(driver = driver)
driver.get( 'https://sandaly.ir/%d8%aa%d9%85%d8%a7%d8%b3-%d8%a8%d8%a7-%d9%85%d8%a7/')
driver.implicitly_wait(3)

login_object.enter_name('Arman Abbasi')
login_object.enter_phonenumber('09191112233')
login_object.enter_message('سلام، این یک محتوای تستی هست')

login_object.click_on_send_button()
sleep(5)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome ( executable_path=ChromeDriverManager().install())
driver.get("https://google.com")
driver.find_element("name",'q').send_keys("hello world")
sleep(5)
driver.quit()  #teardown👆🏻

#session and directory => stop
#cash => clean
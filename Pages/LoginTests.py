
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from login import Login

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

#when we must import a class in a file
# when we want to use a object the have all value of class.
login_object = Login()
#This will go to the practice website and fill out the text boxes, and then press the log in button. The screen will update and then it will click the log out button. Then close. 

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# Navigate to practice
driver.get("http://www.uitestingplayground.com/sampleapp")

time.sleep(1)

#Find the text boxes I am going to input my data
username = driver.find_element(By.CLASS_NAME, 'form-control')
password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")

#input a username and the password
username.send_keys("I am the user!")
password.send_keys("pwd")

#find the button and click it
button = driver.find_element(By.CSS_SELECTOR, "button[id='login'")
button.click()

time.sleep(2)

#Find the logout button and click it
logout = driver.find_element(By.CSS_SELECTOR, "button[id='login']")
logout.click()

#pause and close web page.
time.sleep(2)
driver.quit()






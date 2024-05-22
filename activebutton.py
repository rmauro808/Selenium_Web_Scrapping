#This is a python program that will go to a website and find a button/link to click. After the link has been clicked once the class will change.
#This program is prepared to handle that as it will look for the new class name and then continue to click to the amount of times you'd like. 


from telnetlib import EC

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# Navigate to practice
driver.get("http://www.uitestingplayground.com/mouseover")

#find the first time the button needs to be clicked and click
click_me = driver.find_element(By.CLASS_NAME, "text-primary")
click_me.click()

#find the button after been clicked
active_click = driver.find_element(By.CLASS_NAME, "text-warning")

#click the new button for amount in range
for i in range(99):
    active_click.click()

#sleep to see finished and quit
time.sleep(3)
driver.quit()

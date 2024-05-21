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
driver.get("http://www.uitestingplayground.com/textinput")

#find the form bar
buttonBox = driver.find_element(By.CLASS_NAME, "form-control")

#fill it in
buttonBox.send_keys("Practice Button")
time.sleep(3)

#find submit button and click
submit_button =driver.find_element(By.ID,"updatingButton")
submit_button.click()

time.sleep(5)

#quit the program when comlete with iterations.
driver.quit()

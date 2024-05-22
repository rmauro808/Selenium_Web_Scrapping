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
driver.get("http://www.uitestingplayground.com/progressbar")

time.sleep(1.5)

#Find the start and stop button
start_button = driver.find_element(By.CSS_SELECTOR, "button[id='startButton'")
stop_button = driver.find_element(By.CSS_SELECTOR, "button[id='stopButton']")

#Start the progress bar by clikcing.
start_button.click()

#Loop over and over gathering the progress bar's text and wait for 75%, then break.
while True:
    progress_bar = driver.find_element(By.CSS_SELECTOR, 'div[id="progressBar"]')
    bar_progress = progress_bar.text
    if bar_progress == '75%':
        break

#This will stop the progress bar soon as it hits 75%
stop_button.click()

#Pause to see results and quit.
time.sleep(4)
driver.quit()













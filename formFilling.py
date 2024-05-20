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

#number of times to repeat
repeat = 10

#loop to iterate.
for i in range(repeat):
    # Navigate to practice
    driver.get("https://the-internet.herokuapp.com/login")

    #Find the username and password field.
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    #fill them in
    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")

    #press log in
    password.send_keys(Keys.RETURN)

    try:
        success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
        print("Attempt ", i, "Logged in!", success_message.text)
    except:
        print("Login failed")


    #wait time between iterations.
    time.sleep(1)

#quit the program when comlete with iterations.
driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create Chrome browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# Open Linkedin login page
driver.get("https://www.linkedin.com/login") 
print("Current URL:", driver.current_url)
print("Title:", driver.title)

input("Check the browser and press Enter...")

# Enter email
driver.find_element(By.ID, "username").send_keys("your_test_email@example.com") 
driver.find_element(By.ID, "password").send_keys("your_test_password")

print("linkedin opened successfully!")

input("Press Enter to close the browser...")

driver.quit() 

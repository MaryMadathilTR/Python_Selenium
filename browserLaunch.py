from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")

driver.find_element(By.NAME, "q").send_keys("Automation step by step")
time.sleep(2)
driver.find_element(By.NAME, "btnK").click()
time.sleep(2)
driver.quit()
print("Test Completed")

# Path: test.
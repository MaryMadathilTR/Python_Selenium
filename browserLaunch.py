from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


browserName = "edge"

if browserName == "chrome":
    chrome_options = Options()
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)
elif browserName == "firefox":
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
elif browserName == "edge":
    driver = webdriver.Edge()
elif browserName == "safari":
    driver = webdriver.Safari()
else:
    print("Please pass the correct browser name: " + browserName)
    raise Exception("Driver is not found")

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
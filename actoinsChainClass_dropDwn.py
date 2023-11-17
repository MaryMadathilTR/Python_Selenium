from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui


chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.spicejet.com/")

time.sleep(5)

# Get the mouse coordinates when placed over the top-left corner of the notification
# top_left_coordinates = pyautogui.position()
# print(f"Top-left coordinates: {top_left_coordinates}")
#
# try:
#     pyautogui.moveTo(400,173)
#     pyautogui.click()
#     print("Dismissed the notification alert")
# except Exception as e:
#     print(e)
pyautogui.press("esc")

time.sleep(5)

actions = ActionChains(driver)
add_ons = driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n']//div[text() = 'Add-ons' ]")

actions.move_to_element(add_ons).perform()
time.sleep(2)
spiceMax_addons_link = driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n']//div[@class='css-1dbjc4n r-18u37iz']/a/div/div[text()='SpiceMax']")
spiceMax_addons_link.click()
time.sleep(5)

driver.quit()
print("Test Completed")


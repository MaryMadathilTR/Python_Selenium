from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browserName = "chrome"

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
driver.implicitly_wait(20)
driver.get("https://www.orangehrm.com/")

time.sleep(10)
accept_cookies = driver.find_element(By.XPATH,"//div[@class='optanon-alert-box-button-middle accept-cookie-container']")
accept_cookies.click()
book_a_free_demo_button = driver.find_element(By.XPATH,"//div[@class='d-flex web-menu-btn']//li[1]/a[1]")
book_a_free_demo_button.click()
time.sleep(5)

def select_value_from_dropdown(element, value):
    select = Select(element)
    select.select_by_visible_text(value)

select_country = driver.find_element(By.CSS_SELECTOR,"#Form_getForm_Country")
# select = Select(select_country)
#
# select.select_by_visible_text("India")

select_value_from_dropdown(select_country,"India")

time.sleep(5)

select.select_by_index(3)
time.sleep(5)
driver.quit()
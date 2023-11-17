from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
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


time.sleep(5)
enter_your_email = driver.find_element(By.XPATH,"//input[@placeholder='Enter your email address here']")
enter_your_email.send_keys("Automationstepbystep@gmail.com")
time.sleep(2)
try_it_for_free = driver.find_element(By.NAME,"action_request")
try_it_for_free.click()

time.sleep(5)
homePage = driver.find_element(By.CLASS_NAME,"nav-logo")
homePage.click()
time.sleep(5)

book_a_free_demo_button = driver.find_element(By.XPATH,"//div[@class='d-flex web-menu-btn']//li[1]/a[1]")
                                              # "//div[@class='d-flex web-menu-btn']/ul/li/a/button[text() = 'Book a Free Demo']")
# free_demo_for_title = driver.find_element(By.XPATH,"//div/h4[text() = 'We Just Need a Few Details.']")



time.sleep(5)
book_a_free_demo_button.click()
time.sleep(5)
enter_fullName = driver.find_element(By.ID,"Form_getForm_FullName")
enter_fullName.send_keys("Automation step by step")
time.sleep(2)
get_free_demo= driver.find_element(By.CSS_SELECTOR,"#Form_getForm_action_submitForm")
get_free_demo.click()
time.sleep(5)

privacy_notice = driver.find_element(By.PARTIAL_LINK_TEXT,"Privacy Policy")
privacy_notice.click()
time.sleep(2)
driver.close()



driver.quit()
print("Test Completed")

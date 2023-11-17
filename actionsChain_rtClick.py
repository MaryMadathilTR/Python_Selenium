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
def select_from_rightClickMenu(element,value):
    for ele in element:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

actions = ActionChains(driver)
right_click_ele = driver.find_element(By.XPATH,"//span[text()='right click me']")
actions.context_click(right_click_ele).perform()
right_click_options = driver.find_elements(By.CSS_SELECTOR,"li.context-menu-icon span")
print(len(right_click_options))
select_from_rightClickMenu(right_click_options,"Edit")

pyautogui.press("enter")


time.sleep(2)

driver.quit()
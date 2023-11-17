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

def select_value_from_dropdown(option_list, value):
    if not value[0] == "all":
        for ele in option_list:
            print(ele.text)
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    break
    else:
        for ele in option_list:
            ele.click()


driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

multi_selectionDropDowm = driver.find_element(By.ID,"justAnInputBox")
multi_selectionDropDowm.click()
time.sleep(2)

drop_list = driver.find_elements(By.CLASS_NAME,"ComboTreeItemChlid")
print(len(drop_list))
print(drop_list)
# select_value_from_dropdown(drop_list,"choice 6 2 3")
# select_value_from_dropdown(drop_list,["choice 6 2 3","choice 6 2 2","choice 6 2 1"])
select_value_from_dropdown(drop_list,["all"])
# for ele in drop_list:
#     print(ele.text)
#     if ele.text == "choice 6 2 3":
#         ele.click()
#         break

time.sleep(5)
driver.quit()
print("Test Completed")
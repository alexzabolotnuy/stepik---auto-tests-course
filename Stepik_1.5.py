import os
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

browser.implicitly_wait(13)

button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "10000")
)
button = browser.find_element_by_css_selector("[id = 'book']").click()


# input =  browser.find_element_by_class_name("btn").click()
# new_window = browser.window_handles[1]
# input1_1 = browser.switch_to.window(new_window)
# time.sleep(2)
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
# button = browser.find_element_by_css_selector("button.btn")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
x_element = browser.find_element_by_css_selector("[id = 'input_value']")
x = x_element.text
y = calc(x)
print(y)

input2 = browser.find_element_by_css_selector("[id = 'answer']").send_keys(y)
# input3 = browser.find_element_by_css_selector("input:nth-child(6)").send_keys("asd@asd.com")
# current_dir = os.path.abspath(os.path.dirname('stepik'))
# file_path = os.path.join(current_dir, 'stepik.txt')
# input4 = browser.find_element_by_css_selector("[type = 'file']").send_keys(file_path)


# ?????????? ??????????? ?????
button = browser.find_element_by_css_selector("[id = 'solve']")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

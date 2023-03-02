import time

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


path = '/home/olytvynov/Projects/HL/hl_pyauto_17oct22/drivers/chromedriver_linux64/chromedriver'
driver = Chrome(service=Service(path))
driver.maximize_window()
driver.implicitly_wait(5)

# driver.get('https://www.imgonline.com.ua/eng/combine-two-images-into-one.php')
#
# upload_file = driver.find_element(By.XPATH, "//input[@name='uploadfile']")
# upload_file.send_keys('/home/olytvynov/Projects/HL/hl_pyauto_17oct22/L22_Virtual_environments_PIP_Packages/img.jpg')

# Datepicker

driver.get('https://demo.guru99.com/test/')
date_picker = driver.find_element(By.XPATH, "//input[@name='bdaytime']")
date_picker.send_keys('11012023')
date_picker.send_keys(Keys.TAB)
date_picker.send_keys('0914PM')

# submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
# submit_button.click()

form = driver.find_element(By.XPATH, "//form[@name='bdate']")
form.submit()

time.sleep(3)
driver.quit()

import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


path = '/home/olytvynov/Projects/HL/hl_pyauto_17oct22/drivers/chromedriver_linux64/chromedriver'
driver = Chrome(service=Service(path))
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.saucedemo.com/')

username = driver.find_element(By.ID, 'user-name')
password = driver.find_element(By.ID, 'password')
login_button = driver.find_element(By.ID, 'login-button')

print(driver.get_cookies())
#driver.add_cookie({'name': 'My cookie', 'value': 'QQQQQ'})

import datetime
new_date = int(datetime.datetime.now().timestamp() + 3600)
my_cookie = {'domain': 'www.saucedemo.com', 'expiry': new_date, 'httpOnly': False, 'name': 'session-username', 'path': '/', 'secure': False, 'value': 'standard_user'}
driver.add_cookie(my_cookie)


print(driver.get_cookies())

driver.get('https://www.saucedemo.com/inventory.html')
breakpoint()

# username.send_keys('standard_user')
# password.send_keys('secret_sauce')
# login_button.click()

print(driver.get_cookies())


time.sleep(2)



driver.quit()

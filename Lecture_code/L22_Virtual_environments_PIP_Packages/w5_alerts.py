import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


path = '/home/olytvynov/Projects/HL/hl_pyauto_17oct22/drivers/chromedriver_linux64/chromedriver'
driver = Chrome(service=Service(path))
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demo.guru99.com/test/delete_customer.php")

submit_button = driver.find_element(By.NAME, 'submit')
submit_button.click()
time.sleep(2)
submit_alert = driver.switch_to.alert
print(submit_alert.text)
submit_alert.dismiss()
time.sleep(2)
submit_button.click()
submit_alert.accept()
time.sleep(2)
print(submit_alert.text)
submit_alert.accept()

time.sleep(2)
driver.quit()

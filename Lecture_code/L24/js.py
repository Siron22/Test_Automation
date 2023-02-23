from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

path = '/home/olytvynov/Projects/HL/hl_pyauto_17oct22/drivers/chromedriver_linux64/chromedriver'
driver = Chrome(service=Service(path))
driver.maximize_window()
driver.implicitly_wait(5)



# General formula
# driver.executeScript("javascript code", arguments);

# driver.get('https://demo.guru99.com/test/guru99home/scrolling.html')
# vb_sript = driver.find_element(By.XPATH, "//div[@class='module-content']/div/div[6]")
# driver.execute_script("arguments[0].scrollIntoView();", vb_sript)
# print(driver.execute_script("return document.title;"))
# action = ActionChains(driver)
# action.move_to_element(vb_sript).perform()
#vb_sript.click()


driver.get('http://google.com')
query_input = driver.find_element(By.NAME, 'q')
query_input.send_keys('Croatia')
hint = driver.find_element(By.XPATH, '//ul[@role="listbox"]/li[1]')
hint.click()
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


time.sleep(3)
driver.quit()


import time

from selenium.webdriver import Chrome, Keys, ActionChains
from selenium.webdriver.chrome.service import Service


path = '/home/olytvynov/Projects/HL/hl_pyauto_17oct22/drivers/chromedriver_linux64/chromedriver'
driver = Chrome(service=Service(path))
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://en.wikipedia.org/wiki/Croatia")

action = ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

time.sleep(2)
driver.quit()

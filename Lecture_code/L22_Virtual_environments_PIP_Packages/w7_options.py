import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service


#   https://chromedriver.chromium.org/mobile-emulation
path = '/home/olytvynov/Projects/HL/hl_pyauto_17oct22/drivers/chromedriver_linux64/chromedriver'

options = ChromeOptions()
mobile_emulation = {"deviceName": "Nexus 5"}
options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = Chrome(service=Service(path), options=options)

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://en.wikipedia.org/wiki/Croatia")
print(driver.current_url)
time.sleep(2)
driver.quit()

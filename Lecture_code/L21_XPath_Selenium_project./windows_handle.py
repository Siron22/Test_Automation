import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

try:
    driver.get('https://yahoo.com')
    print(f'Title: "{driver.title}"')

    # Opens a new tab
    driver.execute_script("window.open()")
    driver.execute_script("window.open()")

    print('Tabs:', len(driver.window_handles), driver.window_handles)

    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://google.com')
    print(f'Switch to title: "{driver.title}"')

    time.sleep(2)

    driver.switch_to.window(driver.window_handles[2])
    driver.get('https://ya.ru')
    print(f'Switch to title: "{driver.title}"')

    time.sleep(2)

    driver.switch_to.window(driver.window_handles[0])
    print(f'Switch to title: "{driver.title}"')

    time.sleep(2)

finally:
    driver.quit()
from selenium.webdriver import Chrome, Keys
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


path = '/home/olytvynov/Projects/HL/hl_pyauto_17oct22/drivers/chromedriver_linux64/chromedriver'
#driver = Chrome(executable_path=path)
driver = Chrome(service=Service(path))
driver.maximize_window()
#driver.implicitly_wait(5)

wait = WebDriverWait(driver, 5)

driver.get('http://google.com')
query_input = driver.find_element(By.NAME, 'q')
query_input.send_keys('Croatia')


hint = wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@role="listbox"]/li[1]')))
#time.sleep(3)
#hint = driver.find_element(By.XPATH, '//ul[@role="listbox"]/li[1]')
hint.click()

# links_titles = driver.find_elements(By.TAG_NAME, 'h3')
# #print(links_titles)
# for link_title in links_titles:
#     print(link_title.text)

result_query = driver.find_element(By.NAME, 'q')
print(result_query.get_attribute('value'))
print(result_query.get_property('value'))
print()

# result_query.clear()
# result_query.send_keys('Another text')
# for i in range(3):
#     result_query.send_keys(Keys.BACKSPACE)
# result_query.send_keys(Keys.ENTER)

# map = driver.find_element(By.XPATH, '//img[@id="lu_map"]')
# print(map.get_attribute('width'))
# print(map.get_property('width'))

wiki_link = driver.find_element(By.XPATH, "//div[@class='hlcw0c']/descendant::div[@class='yuRUbf']/a[contains(@href, 'wiki')]")
wiki_link.click()

#driver.save_screenshot('page.png')


flag = driver.find_element(By.XPATH, "//td[@class='infobox-image']")
flag.screenshot('flag.png')

# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()


# print(driver.name)
# print(driver.current_url)
# print(driver.title)
# print()
# print(driver.page_source)


# link = driver.find_element(By.LINK_TEXT, 'twenty counties')
# link.click()

# link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Croat')
# link.click()

time.sleep(4)
driver.quit()

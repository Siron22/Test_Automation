import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


path = '/home/olytvynov/Projects/HL/hl_pyauto_17oct22/drivers/chromedriver_linux64/chromedriver'
driver = Chrome(service=Service(path))
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://demo.guru99.com/test/newtours/register.php')
countries_dropdown_element = driver.find_element(By.NAME, 'country')
countries_dropdown = Select(countries_dropdown_element)
#print(countries_dropdown.options)
# for option in countries_dropdown.options:
#     print(option.text)

print(countries_dropdown.is_multiple)
countries_dropdown.select_by_index(3)
print(countries_dropdown.all_selected_options[0].text)
time.sleep(2)
countries_dropdown.select_by_value("ANTARCTICA")
print(countries_dropdown.all_selected_options[0].text)
time.sleep(2)
countries_dropdown.select_by_visible_text("CHAD")
print(countries_dropdown.all_selected_options[0].text)

# Multiple

# driver.get('https://output.jsbin.com/osebed/2')
# fruits_element = driver.find_element(By.ID, 'fruits')
# fruits = Select(fruits_element)
#
# print(fruits.is_multiple)
#
# fruits.select_by_visible_text("Orange")
# fruits.select_by_index(0)
# print([fruit.text for fruit in fruits.all_selected_options])
# fruits.deselect_by_index(0)
# print([fruit.text for fruit in fruits.all_selected_options])
#
# fruits.select_by_visible_text("Grape")
# print([fruit.text for fruit in fruits.all_selected_options])
# time.sleep(2)
#
# fruits.deselect_all()
# print([fruit.text for fruit in fruits.all_selected_options])
#
# #time.sleep(2)

time.sleep(2)
driver.quit()

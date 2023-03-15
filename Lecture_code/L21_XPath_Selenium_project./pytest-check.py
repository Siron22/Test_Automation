from pytest_check import check
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import pytest_check as check

# def test_check():
#     with pytest_check.check:
#         #with pytest_check.raises(Exception):
#             #raise Exception("Exception raised")
#         assert 1 == 2, "Failed 1==2"
#     with pytest_check.check:
#         assert 2 == 2
#     with pytest_check.check:
#         assert 2 == 5, "Failed 2==5"

def test_register_user():
    # Arrange
    url = "https://docket-test.herokuapp.com/register"
    # set the driver instance
    driver = webdriver.Chrome()
    # browse to the endpoint
    driver.get(url)
    # maximise the window
    driver.maximize_window()
    # Act
    # Complete registration form
    # enter username value
    driver.find_element(By.ID, "username").send_keys("Ryan8")
    # enter email value
    driver.find_element(By.ID, "email").send_keys("Test@email8.com")
    # enter password value
    driver.find_element(By.ID, "password").send_keys("12345")
    # enter repeat password value
    driver.find_element(By.ID, "password2").send_keys("12345")
    # click register button
    driver.find_element(By.ID, "submit").click()
    # Assert
    # confirm registration has been successful
    # check if congratulations message contains the correct text
    message = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]").text
    check.equal(message, "Congratulations, you are now registered")
    # check user is routed to login page
    current_url = driver.current_url
    check.is_in("login", current_url)
    driver.quit()



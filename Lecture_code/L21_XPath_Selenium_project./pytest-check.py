import pytest_check


def test_check():
    with pytest_check.check:
        #with pytest_check.raises(Exception):
            #raise Exception("Exception raised")
        assert 1 == 2, "Failed 1==2"
    with pytest_check.check:
        assert 2 == 2
    with pytest_check.check:
        assert 2 == 5, "Failed 2==5"




# def test_pytest_check():
#     with pytest_check.check:
#         assert 2 == 3
#     check.equal(2, 3)
#     assert True

# @allure.description('Test for all main paige elements visibility')
# def test_main_page_elements_displayed(driver):
#     main_page = MainPage(driver)
#     main_page.navigate_to_main()
#     pytest_check.check.is_true(main_page.video_locator.is_displayed())
#     with pytest_check.check:
#         assert main_page.logo_hillel_auto.is_displayed()
#     with pytest_check.check:
#         assert main_page.button_home.is_displayed()
#     with pytest_check.check:
#         assert main_page.button_about.is_displayed()
#     with pytest_check.check:
#         assert main_page.button_contacts.is_displayed()
#     with pytest_check.check:
#         assert main_page.button_guest_login.is_displayed()
#     with pytest_check.check:
#         assert main_page.button_signin.is_displayed()
#     with pytest_check.check:
#         assert main_page.button_signup.is_displayed()
#     with pytest_check.check:
#         assert main_page.string1.is_displayed()
#     with pytest_check.check:
#         assert main_page.string2.is_displayed()
#      pytest_check.check.is_true(main_page.video_locator.is_displayed())
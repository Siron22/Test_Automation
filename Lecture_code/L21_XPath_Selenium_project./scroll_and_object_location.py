
def test_main_page_scroll_to_end(driver, main_page):
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    import time
    time.sleep(2)


def test_main_page_click_about(driver, main_page):
    """trial test for the location of the object on the page"""
    import time
    print('Window rect: ', driver.get_window_rect())
    print('Email location: ', main_page.link_email.location)
    print('Link email: ', driver.execute_script("return arguments[0].getBoundingClientRect();", main_page.link_email))  # {'bottom': 1286.09375, 'height': 19, 'left': 1356.671875, 'right': 1506.5, 'toJSON': {}, 'top': 1267.09375, 'width': 149.828125, 'x': 1356.671875, 'y': 1267.09375}
    time.sleep(1)
    main_page.click_button_about()
    time.sleep(1)
    print('Window rect: ', driver.get_window_rect())
    print('Email location: ',main_page.link_email.location)
    print('Link email: ',driver.execute_script("return arguments[0].getBoundingClientRect();", main_page.link_email))  # {'bottom': 701.09375, 'height': 19, 'left': 1356.671875, 'right': 1506.5, 'toJSON': {}, 'top': 682.09375, 'width': 149.828125, 'x': 1356.671875, 'y': 682.09375}



import allure
import pytest


@pytest.fixture
def user():
    return 'AAAA'

@pytest.fixture
def setup():
    print(23232323)
    yield
    print(56767553)





@allure.step('Perform entering name: {0}')
def enter_name(name):
    pass



@allure.step('Perfrom entering password {password}')
def enter_password(password):
    pass

@allure.step
def click_login():
    pass

@allure.epic('MyEpic')
@allure.feature('Login')
@allure.story('Successful login')
def test_login(user, setup):
    enter_name('John')
    enter_password('qweereredfdfdd')
    click_login()



@allure.link('http://google.com', name='Click me')
@allure.issue('http://google.com', name='BUG-123')
@allure.testcase('http://google.com', name='TC-1233')
@allure.title('PASSING TEST')
@allure.description('This test is about')
@allure.severity(allure.severity_level.BLOCKER)
def test_that_pass():
    assert True




@allure.epic('MyEpic')
@allure.description('Static description')
@allure.severity(allure.severity_level.CRITICAL)
def test_that_fail():
    param = 111
    allure.dynamic.description(f"Test was performed with  {param}")

    assert False


def test_attachments():
    allure.attach.file('tests/img.jpg', name='Attachment', attachment_type=allure.attachment_type.JPG)
    allure.attach('Text rtrrrrrrrrrrrrrrrrrrrrr', name='My Test', attachment_type=allure.attachment_type.TEXT)
    allure.attach('<html><body><h1>TITLE</h1> TESTS</body></html>')

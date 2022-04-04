from conftest import param
import methods
from faker import Faker
import allure


@allure.feature('Login')
@allure.story('Login with invalid credentials')
@allure.severity(allure.severity_level.BLOCKER)
def test_login_invalid_credentials(driver, config):
    faker = Faker() 
    with allure.step('Click "Login" Link'):
        methods.LoginPage.click_login_link(driver, config)

    with allure.step('Enter invalid Username'):
        invalid_username = faker.name()
        methods.LoginPage.enter_username(driver, config, invalid_username)

    with allure.step('Enter invalid Password'):
        invalid_password = faker.password()
        methods.LoginPage.enter_password(driver, config, invalid_password)

    with allure.step('Click "Login" button'):
        methods.LoginPage.click_login_button(driver, config)

    with allure.step('Check, that Alert message appears'):
        success = methods.LoginPage.get_loginfailed_message(driver)
        assert success == driver.switch_to.alert.text


@allure.feature('Login')
@allure.story('Login and Logout valid credentials')
@allure.severity(allure.severity_level.BLOCKER)
def test_login_logout(driver, config, param):

    with allure.step('Click "Login" Link'):
        methods.LoginPage.click_login_link(driver, config)

    with allure.step('Get Username and Password for the Login page'):
        username, password = methods.LoginPage.get_credentials(param)

    with allure.step('Enter valid Username'):
        methods.LoginPage.enter_username(driver, config, username)

    with allure.step('Enter valid Password'):
        methods.LoginPage.enter_password(driver, config, password)

    with allure.step('Click "Login" button'):
        methods.LoginPage.click_login_button(driver, config)

    with allure.step('Check, that login message appears'):
        greeting = methods.LoginPage.get_loginSuccess_message(driver, config)
        print('Greetings---',greeting)
        assert greeting == f'Welcome {username}'
        
    with allure.step('Press Logout button'):
        methods.LoginPage.click_logout_button(driver, config)
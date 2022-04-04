import methods
import allure


@allure.feature('SignUp')
@allure.story('Sign')
@allure.severity(allure.severity_level.BLOCKER)
def test_signup(driver, config):

    with allure.step('Click "SignUp" Link'):
        methods.SignPage.click_signup_link(driver, config)

    with allure.step('Enter Username'):
        methods.SignPage.enter_username(driver, config, 'NewUser10c')

    with allure.step('Enter Password'):
        methods.SignPage.enter_password(driver, config, 'asdfghj')

    with allure.step('Click "SignUp" button'):
        methods.SignPage.click_signup_button(driver, config)

    with allure.step('Check, that Success message appears'):
        success = methods.SignPage.get_signupSuccess_message(driver)
        print('This is the alert message', success)
        assert success == driver.switch_to.alert.text
        
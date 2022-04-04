import methods
import allure


@allure.feature('ContactUs')
@allure.story('Send a message')
@allure.severity(allure.severity_level.BLOCKER)
def test_contactus(driver, config):

    with allure.step('Click "ContactUS" Link'):
        methods.ContactPage.click_contactus_link(driver, config)

    with allure.step('Enter Email'):
        methods.ContactPage.enter_email(driver, config, 'jon@test.com')

    with allure.step('Enter Name'):
        methods.ContactPage.enter_name(driver, config, 'Jon')
    
    with allure.step('Enter Message'):
        methods.ContactPage.enter_message(driver, config, 'This is just a test')

    with allure.step('Click SendMessage button'):
        methods.ContactPage.click_sendmessage_button(driver, config)

    with allure.step('Check, that Success message appears'):
        success = methods.ContactPage.get_success_message(driver)
        print('This is the alert message', success)
        assert success == driver.switch_to.alert.text
        
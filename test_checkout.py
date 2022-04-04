import methods
import allure


@allure.feature('Shopping-Checkout')
@allure.story('Checkout carted products')
@allure.severity(allure.severity_level.BLOCKER)
def test_checkout(driver, config):
# checkout
    with allure.step('Enter Name'):
        methods.ShopPage.enter_name(driver, config, 'Jon')

    with allure.step('Enter City'):
        methods.ShopPage.enter_country(driver, config, 'NYC')

    with allure.step('Enter Card'):
        methods.ShopPage.enter_card(driver, config, '3252272777272')
    
    with allure.step('Enter Month'):
        methods.ShopPage.enter_month(driver, config, '09')
    
    with allure.step('Enter Year'):
        methods.ShopPage.enter_year(driver, config, '2022')
        
    with allure.step('Click Purchase button'):
        methods.ShopPage.click_purchase_button(driver, config)
        
    # with allure.step('Check, that Success message appears'):
    #     success = methods.ShopPage.get_signupSuccess_message(driver)
    #     assert success == driver.switch_to.alert.text
        
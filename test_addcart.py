import methods
import allure


@allure.feature('Shopping-Add2Cart')
@allure.story('Add to cart')
@allure.severity(allure.severity_level.BLOCKER)
def test_addcart(driver, config, param, login):
    with allure.step('Click Category Link'):
        methods.ShopPage.click_category_link(driver, config, 'Phone')

    with allure.step('Select Phones'):
        methods.ShopPage.click_phone_link(driver, config, param)

    with allure.step('Click Category Link'):
        methods.ShopPage.click_category_link(driver, config, 'Laptop')

    with allure.step('Select Laptop'):
        methods.ShopPage.click_laptop_link(driver, config, param)
    
    with allure.step('Click Category Link'):
        methods.ShopPage.click_category_link(driver, config, 'Monitor')
 
    with allure.step('Select Monitor'):
        methods.ShopPage.click_monitor_link(driver, config, param)
import time, random
from unicodedata import category
from pytest import param

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

WAIT = 1
WAIT_SEL = 10


def find_by_xpath(driver, xpath):
    time.sleep(WAIT)
    wait = WebDriverWait(driver, WAIT_SEL)
    el = None
    try:
        el = wait.until(ec.presence_of_element_located((By.XPATH, xpath)))
    except NoSuchElementException as e:
        assert 'Following XPATH is not found: "{}". Exception: {}'.format(xpath, e)
    return el


def accept_alert(driver):
    WebDriverWait(driver, WAIT_SEL).until(ec.alert_is_present())
    alert = driver.switch_to_alert()
    alert.accept()
    
class LoginPage:
    @staticmethod
    def click_login_link(driver, config):
        find_by_xpath(driver, config['LOCATORS-LOGIN']['LoginLink']).click()

    @staticmethod
    def enter_username(driver, config, value):
        el = find_by_xpath(driver, config['LOCATORS-LOGIN']['UsernameField'])
        el.clear()
        el.send_keys(value)

    @staticmethod
    def enter_password(driver, config, value):
        el = find_by_xpath(driver, config['LOCATORS-LOGIN']['PasswordField'])
        el.clear()
        el.send_keys(value)

    @staticmethod
    def click_login_button(driver, config):
        find_by_xpath(driver, config['LOCATORS-LOGIN']['LoginButton']).click()

    @staticmethod
    def click_logout_button(driver, config):
        find_by_xpath(driver, config['LOCATORS-LOGIN']['LogoutButton']).click()

    
    @staticmethod
    def get_loginSuccess_message(driver, config):
        el = find_by_xpath(driver, config['LOCATORS-LOGIN']['LoginConfirmation'])
        time.sleep(4)
        return el.text
    
    @staticmethod
    def get_loginfailed_message(driver):
        time.sleep(5)
        el = driver.switch_to.alert
        return el.text
    
    @staticmethod
    def get_credentials(param):
        username = param['DETAILS']['username']
        password = param['DETAILS']['password']
        return username, password
    
    
class SignPage:
    @staticmethod
    def click_signup_link(driver, config):
        find_by_xpath(driver, config['LOCATORS-SIGNUP']['SignUpLink']).click()

    @staticmethod
    def enter_username(driver, config, value):
        el = find_by_xpath(driver, config['LOCATORS-SIGNUP']['UsernameField'])
        el.clear()
        el.send_keys(value)

    @staticmethod
    def enter_password(driver, config, value):
        el = find_by_xpath(driver, config['LOCATORS-SIGNUP']['PasswordField'])
        el.clear()
        el.send_keys(value)

    @staticmethod
    def click_signup_button(driver, config):
        find_by_xpath(driver, config['LOCATORS-SIGNUP']['SignUpButton']).click()

    @staticmethod
    def get_signupSuccess_message(driver):
        time.sleep(5)
        el = driver.switch_to.alert
        return el.text
    
    
class ContactPage:
    @staticmethod
    def click_contactus_link(driver, config):
        find_by_xpath(driver, config['LOCATORS-HEADER']['contactLink']).click()

    @staticmethod
    def enter_email(driver, config, value):
        el = find_by_xpath(driver, config['LOCATORS-CONTACTUS']['EmailField'])
        el.clear()
        el.send_keys(value)

    @staticmethod
    def enter_name(driver, config, value):
        el = find_by_xpath(driver, config['LOCATORS-CONTACTUS']['NameField'])
        el.clear()
        el.send_keys(value)

    @staticmethod
    def enter_message(driver, config, value):
        el = find_by_xpath(driver, config['LOCATORS-CONTACTUS']['MessageField'])
        el.clear()
        el.send_keys(value)

    @staticmethod
    def click_sendmessage_button(driver, config):
        find_by_xpath(driver, config['LOCATORS-CONTACTUS']['SendMessageButton']).click()

    @staticmethod
    def get_success_message(driver):
        el = driver.switch_to.alert
        return el.text
    

class ShopPage:
    @staticmethod
    def click_category_link(driver, config, category):
        catg = category
        find_by_xpath(driver, config['LOCATORS-CATEGORIES'][f'{category}Link']).click()
        return catg
    
    @staticmethod
    def click_phone_link(driver, config, param):
    
        find_by_xpath(driver, config['LOCATORS-CATEGORIES']['PhoneLink']).click()
        n = random.randint(int(param['PHONE']['start']), int(param['PHONE']['end']))

        # find_by_xpath(driver, f'//a[@href="/prod.html?idp_={n}"]').click()
        driver.find_element_by_css_selector(f'#tbodyid > div:nth-child({n}) > div > div > h4 > a').click()
        time.sleep(4)
        
        find_by_xpath(driver, config['LOCATORS-CART']['AddCartButton']).click()
        find_by_xpath(driver, config['LOCATORS-CART']['CartLink']).click()
        find_by_xpath(driver, config['LOCATORS-CART']['PlaceOrderButton']).click()
                    
    @staticmethod
    def click_laptop_link(driver, config, param):
        find_by_xpath(driver, config['LOCATORS-CATEGORIES']['LaptopLink']).click()
        n = random.randint(int(param['LAPTOP']['start']), int(param['LAPTOP']['end']))
        # find_by_xpath(driver, f'//a[@href="/prod.htmlidp_={n}').click()
        driver.find_element_by_css_selector(f'#tbodyid > div:nth-child({n}) > div > div > h4 > a').click()
        time.sleep(4)
        find_by_xpath(driver, config['LOCATORS-CART']['AddCartButton']).click()
        time.sleep(2)
        driver.switch_to.alert.dismis()
        time.sleep(2)
        # find_by_xpath(driver, config['LOCATORS-CART']['CartLink']).click()
        # find_by_xpath(driver, config['LOCATORS-CART']['PlaceOrderButton']).click()
        
    @staticmethod
    def click_monitor_link(driver, config, param):
        find_by_xpath(driver, config['LOCATORS-CATEGORIES']['MonitorLink']).click()
        n = random.randint(int(param['MONITOR']['start']), int(param['MONITOR']['end']))
        # find_by_xpath(driver, f'//a[@href="/prod.htmlidp_={n}').click()
        driver.find_element_by_css_selector(f'#tbodyid > div:nth-child({n}) > div > div > h4 > a').click()
        time.sleep(4)
        
        find_by_xpath(driver, config['LOCATORS-CART']['AddCartButton']).click()
        time.sleep(2)
        driver.switch_to.alert.dismis()
        time.sleep(2)
        # find_by_xpath(driver, config['LOCATORS-CART']['CartLink']).click()
        # find_by_xpath(driver, config['LOCATORS-CART']['PlaceOrderButton']).click()
    
    @staticmethod
    def enter_name(driver, config, value):
        el = find_by_xpath(driver, config['LOCATOR-CART']['NameField'])
        el.clear()
        el.send_keys(value)

    @staticmethod
    def enter_country(driver, config, value):
        el = find_by_xpath(driver, config['LOCATOR-CART']['CountryField'])
        el.clear()
        el.send_keys(value)

    @staticmethod
    def enter_city(driver, config, value):
        el = find_by_xpath(driver, config['LOCATOR-CART']['CityField'])
        el.clear()
        el.send_keys(value)

    @staticmethod
    def enter_card(driver, config, value):
        el = find_by_xpath(driver, config['LOCATOR-CART']['CreditCardField']).click()
        el.clear()
        el.send_keys(value)
        
    @staticmethod
    def enter_month(driver, config, value):
        el =find_by_xpath(driver, config['LOCATOR-CART']['MonthField']).click()
        el.clear()
        el.send_keys(value)
        
    @staticmethod
    def enter_year(driver, config, value):
        el = find_by_xpath(driver, config['LOCATOR-CART']['YearField']).click()
        el.clear()
        el.send_keys(value)

    @staticmethod
    def click_purchase_button(driver, config):
        find_by_xpath(driver, config['LOCATOR-CART']['PurchaseButton']).click()

    @staticmethod
    def get_success_message(driver):
        el = driver.switch_to.alert
        return el.text

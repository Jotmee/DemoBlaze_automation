from email import message
import os
from unicodedata import category
import pytest
import methods
import configparser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='module')
def config():
    cfg = configparser.ConfigParser()
    cfg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.cfg')
    cfg.read(cfg_path)
    return cfg

@pytest.fixture(scope='module')
def param():
    prm = configparser.ConfigParser()
    prm_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'params.cfg')
    prm.read(prm_path)
    return prm

@pytest.fixture(scope='function')
def driver(config):

    # Launch Driver
    option = webdriver.ChromeOptions()
    #disable popup notifications
    # option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2 })
    dr =  webdriver.Chrome(ChromeDriverManager().install(), options=option)
    #get Url from config file
    dr.get(config['SITE']['URL'])
    # Pass Driver instance to test
    yield dr
    # Quit Driver
    dr.quit()

@pytest.fixture(scope='function')
def login(driver, config, param):
    methods.LoginPage.click_login_link(driver, config)
    username, password = methods.LoginPage.get_credentials(param)
    methods.LoginPage.enter_username(driver, config, username)
    methods.LoginPage.enter_password(driver, config, password)
    methods.LoginPage.click_login_button(driver, config)
    greeting = methods.LoginPage.get_loginSuccess_message(driver, config)
    assert greeting == f'Welcome {username}'
    # message = methods.LoginPage.get_loginfailed_message(driver)
    # assert message == 'Wrong password.' or message == 'User does not exist.'
    

@pytest.fixture(scope='function')
def signup(driver, config):
    methods.SignPage.enter_username(driver, config, '')
    methods.SignPage.enter_password(driver, config, '')
    methods.SignPage.click_login_button(driver, config)
    message = methods.SignPage.get_loginfailed_message(driver)
    assert message == 'Sign up successful.'
    
    
@pytest.fixture(scope='function')
def contactus(driver, config):

    methods.ContactPage.enter_email(driver, config, '')
    methods.ContactPage.enter_name(driver, config, '')
    methods.ContactPage.enter_message(driver, config, '')
    
    methods.ContactPage.click_sendmessage_button(driver, config)
    message = methods.ContactPage.get_success_message(driver)
    assert message == 'Thanks for the message!!'
    
@pytest.fixture(scope='function')
def addcart(driver, config, category, param):
    methods.ShopPage.click_category_link(driver, config, category)
    
    methods.ShopPage.click_phone_link(driver, config, category, param)
    methods.ShopPage.click_laptop_link(driver, config, category, param)
    methods.ShopPage.click_monitor_link(driver, config, category, param)

@pytest.fixture(scope='function')
def checkout(driver, config, addcart):
    methods.ShopPage.enter_name(driver, config, '')
    methods.ShopPage.enter_country(driver, config, '')
    methods.ShopPage.enter_city(driver, config, '')
    methods.ShopPage.enter_card(driver, config, '')
    methods.ShopPage.enter_month(driver, config, '')
    methods.ShopPage.enter_year(driver, config, '')
    methods.ShopPage.click_purchase_button(driver, config)
    
    # message = methods.ContactPage.get_success_message(driver)
    # assert message == ''
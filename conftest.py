import pytest
import requests

from selenium import webdriver

from helpers.helpers import Helpers
from pages.feed import FeedOrderPage
from pages.main import MainPage
from pages.profile import ProfilePage
from pages.login import LoginPage
from helpers.data import API, MAIN_PAGE, Ingredients


@pytest.fixture(params=['chrome', 'firefox']) 
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    driver.get(MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver)

@pytest.fixture
def feed_page(driver):
    return FeedOrderPage(driver)


@pytest.fixture
def user():                                
    email, pwd, name = Helpers().generate_user()
    payload = {
        'email': email,
        'password': pwd,        
        'name': name
    }
    response = requests.post(API.CREATE_USER, data=payload)
    yield email, pwd
    token = response.json()['accessToken']
    requests.delete(API.DELETE_DATA, headers={'Authorization': f'{token}'})


@pytest.fixture
def log_in_with_order(user):
    email, password = user
    payload = {
        'email': email,
        'password': password,
    }
    response = requests.post(API.LOGIN_USER, data=payload)
    token = response.json()['accessToken']
    payload = {
        'ingredients': [Ingredients.BUN_R2_D3, Ingredients.MAIN_PROTOSTOMIA, Ingredients.SAUSE_SPICY_X]
    }
    response = requests.post(API.CREATE_ORDER, headers={'Authorization': f'{token}'}, json=payload)
    number = str(response.json()['order']['number'])
    return email, password, number


import pytest
from selenium.webdriver.support.wait import WebDriverWait
import time
from config import BASE_URL, BASE_URL1, BASE_URL_BUY
from page.page_custom_login import PageLoginCustom
from page.page_login import PageLogin
from page.page_product_search import PageCustomBuy
from tools import DriverTools

#---------------登录前置---------------
@pytest.fixture(scope="function")
def run_login_test():
    driver = DriverTools.get_driver()
    yield driver
    DriverTools.quit_driver()
#---------------进入登陆界面---------------
@pytest.fixture(scope="class")
def run_every_test():
    driver = DriverTools.get_driver()
    yield driver
    DriverTools.quit_driver()
#打开登录界面完成登录并跳转
@pytest.fixture(scope="class")
def run_login(run_every_test):
    driver = run_every_test
    driver.get(BASE_URL)#打开登录界面
    PageLogin(driver).login("admin", "111111", "1111")
    time.sleep(1)
    return driver#返回登录完成界面
#---------------注册会员前置---------------
#打开登录后界面
@pytest.fixture(scope="function")
def run_add_vip(run_login):
    run_login.get(BASE_URL1)#在登录完成界面打开登录完成网址
    time.sleep(1)
    yield run_login
#---------------商品购买前置---------------
@pytest.fixture(scope="class")
#先登录
def run_add_product(run_every_test):
    driver = run_every_test
    driver.get(BASE_URL_BUY)  # 打开登录界面
    PageLoginCustom(driver).login_custom("19071992915", "1111", "1111")
    time.sleep(1)
    return driver  # 返回登录完成界面
@pytest.fixture(scope="function")
def buy_product(run_add_product):
    run_add_product.get(BASE_URL_BUY)#在登录完成界面打开登录完成网址
    PageCustomBuy(run_add_product).search_product("111")
    time.sleep(1)
    yield run_add_product
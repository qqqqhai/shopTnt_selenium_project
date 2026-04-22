

import pytest
from selenium.webdriver.support.wait import WebDriverWait
import time
from config import BASE_URL, BASE_URL1
from page.page_login import PageLogin
from tools import DriverTools

#---------------登录前置---------------
@pytest.fixture(autouse=True)
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
#---------------店铺注册前置---------------
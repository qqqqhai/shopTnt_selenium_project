import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from script import log

from config import BASE_URL_SELLER
from page.page_shell_add_production import PageAddProduction
from tools import read_json, DriverTools
@pytest.fixture(scope="class")
def login_production():
    driver = DriverTools.get_driver()
    driver.get(BASE_URL_SELLER)
    WebDriverWait(driver, 10, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div/form/div[1]/div/div/input'))).send_keys("qhai")
    WebDriverWait(driver, 10, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div/form/div[2]/div/div/input'))).send_keys("255834")
    WebDriverWait(driver, 10, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div/form/div[3]/div/div/div/input'))).send_keys("1111")
    WebDriverWait(driver, 10, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div/form/div[4]/div/button'))).click()
    time.sleep(5)
    yield driver

class TestProduction:

    @pytest.mark.parametrize("add_class,select_name,select_num,select_price1,select_price2,select_weight",read_json("add_production_data.json"))
    def test_add_production_success(self,login_production,add_class,select_name,select_num,select_price1,select_price2,select_weight):
        driver = login_production
        PageAddProduction(driver).add_production(add_class,select_name,select_num,select_price1,select_price2,select_weight)
        expect = PageAddProduction(driver).jug_add_msg()
        log.info(f"结果:{expect}")
        assert expect == "上架商品成功"
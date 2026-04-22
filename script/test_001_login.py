import pytest

from base.conftest import run_login_test
from config import BASE_URL
from page.page_login import PageLogin, jud_handles
from tools import DriverTools, GetLog, read_json
from script import log
from base import conftest

class TestLogin:
    @pytest.mark.parametrize("user_name,password,img_pwd,expect",read_json("login_data.json"))
    def test_01_login_success(self,run_login_test,user_name,password,img_pwd,expect):
        driver=run_login_test
        driver.get(BASE_URL)
        PageLogin(driver).login(user_name,password,img_pwd)
        if expect:
            res = jud_handles(driver=DriverTools.get_driver()).jud_handles_jump()
            log.info(f"登录结果:{res}")
            assert expect == res
        else:
            error_msg = jud_handles(driver=DriverTools.get_driver()).alter_jud()
            log.info(f"登录结果：登陆失败  原因：{error_msg}")




import time

import pytest

from config import BASE_URL_BUY
from page.page_custom_login import PageLoginCustom
from script import log
from tools import read_json
from base.conftest import run_login_test

class TestLogin:
# "pho_num": "190000000000", "img_email": "12345","email_input": "1111","expect": true
    @pytest.mark.parametrize("pho_num,img_email,email_input,expect",read_json("custom_login_data.json"))
    def test_03_login_success(self,run_login_test,pho_num,img_email,email_input,expect):
        driver=run_login_test
        driver.get(BASE_URL_BUY)
        PageLoginCustom(driver).login_custom(pho_num,img_email,email_input)
        time.sleep(2)
        if expect:
            res = PageLoginCustom(driver).jug_login_success()
            log.info(f"登录结果:{expect}")
            assert "我的账户" == res
        else:
            error_msg = PageLoginCustom(driver).jug_login_err()
            log.info(f"登录结果：登陆失败  原因：{error_msg}")



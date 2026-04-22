import pytest
from page.page_add_vip import PageAddVip
from tools import  read_json
from script import log
from base.conftest import run_add_vip,run_login,run_every_test

class TestLogin:
    @pytest.mark.parametrize("vip_name,vip_en_pwd,vip_pwd,vip_phone,sex,expect,a",read_json("add_vip_data.json"))
    def test_01_add_vip_success(self,run_add_vip,vip_name,vip_en_pwd,vip_pwd,vip_phone,sex,expect,a):
        driver =run_add_vip
        PageAddVip(driver).add_vip(vip_name, vip_en_pwd, vip_pwd, vip_phone, sex)
        msg = PageAddVip(driver).jug_add_msg()
        errors = PageAddVip(driver).jug_add_vip(a)
        if expect is True:
                # 预期是成功的 (True)，所以错误信息必须为空 (None)
            log.info(f"注册结果:{msg}")
            assert errors is None, f"测试失败：预期成功，但出现了错误 ->{errors}"
        else:
                # 预期是失败的 (False)，所以错误信息必须存在 (不为 None)
            log.info(f"捕获到的错误信息: {errors}")
            assert errors is not None, f"测试失败：预期应该报错，但没有检测到错误"
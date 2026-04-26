import pytest

from page.page_buy_product import PageProductBuy
from script import log
from tools import read_json


class TestBuy:
    @pytest.mark.parametrize("search,buy_select,time,expect",read_json("production_buy_data.json"))
    def test_03_buy(self,buy_product,buy_select,time,expect):
        driver=buy_product
        PageProductBuy(driver).buy(buy_select,time)
        log.info(f"登录结果:{expect}")
        assert PageProductBuy(driver).jug() == "收银台"

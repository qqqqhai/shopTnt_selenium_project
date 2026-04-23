import time
import pytest
from config import BASE_URL_BUY
from page.page_product_search import PageCustomBuy
from script import log
from tools import read_json
from script.conftest import run_login_test

class TestLogin:
# "pho_num": "190000000000", "img_email": "12345","email_input": "1111","expect": true
    @pytest.mark.parametrize("search_name,search_product,expect",read_json("search_product.json"))
    def test_03_search_success(self,run_login_test,search_name,search_product,expect):
        driver=run_login_test
        driver.get(BASE_URL_BUY)
        PageCustomBuy(driver).search_product(search_name)
        time.sleep(2)
        if expect:
            num=PageCustomBuy(driver).product_num_count()
            frist_product = PageCustomBuy(driver).jug_product_first_name()
            log.info(f"搜索结果:{num}商品,第一个商品名字为:{frist_product}")
            #实际结果大于0
            pass
        else:
            res = PageCustomBuy(driver).jug_product_err()
            log.info(f"搜索结果:{res}")
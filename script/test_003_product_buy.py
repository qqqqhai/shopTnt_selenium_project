from page.page_buy_product import PageProductBuy


class TestBuy:
    def test_03_buy(self,buy_product):
        driver=buy_product
        PageProductBuy(driver).buy()

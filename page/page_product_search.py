import time

from selenium.webdriver.common.by import By

from base.base import BasePage


class PageCustomBuy(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        #点击登录
        self.search=(By.XPATH,'//*[@id="search"]/div[1]/input')

        self.btn_search=(By.XPATH,'//*[@id="search"]/div[1]/button')
        self.product_name=(By.XPATH,'//*[@id="goods-list"]/div/div[2]/div[2]/ul/li/div/div[3]/a/em')
        #页面搜索第一个元素标题
        self.first_product_name=(By.XPATH,'//*[@id="goods-list"]/div/div[2]/div[2]/ul/li[1]/div/div[3]/a/em')
        #//*[@id="goods-list"]/div/div[2]/div[2]/ul/li[1]/div/div[3]/a/em
        #//*[@id="goods-list"]/div/div[2]/div[2]/ul/li[3]/div/div[3]/a/em
        #//*[@id="goods-list"]/div/div[2]/div[2]/ul/li[2]/div/div[3]/a/em
        #商品搜索不到显示信息
        self.product_not_found=(By.XPATH,'//*[@id="goods-list"]/div/div[2]/div[2]/div[1]')
        #商品数量
        self.product_num=(By.XPATH,'//*[@id="goods-list"]/div/div[2]/div[2]/div/span')
    def search_product(self,product):
        self.base_input(self.search,product)
        self.base_click(self.btn_search)

#判断搜索信息
    def jug_product_err(self):
        try:
            return self.fd_element(self.product_not_found).text
        except:
            return None
#判断第一个商品信息
    def jug_product_first_name(self):
        try:
            return self.fd_element(self.first_product_name).text
        except:
            return None
#判断商品数量
    def product_num_count(self):
        try:
            self.scroll_to_bottom()
            time.sleep(1)
            return self.fd_element(self.product_num).text
        except:
            return None
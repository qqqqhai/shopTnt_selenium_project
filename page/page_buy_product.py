import time

from selenium.webdriver.common.by import By

from base.base import BasePage


class PageProductBuy(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        #点击商品
        self.production_click=(By.XPATH,'//*[@id="goods-list"]/div/div[2]/div[2]/ul/li/div')
        self.btn_site=(By.XPATH,'//*[@id="AS-122"]/div/div[1]')
        self.btn_buy=(By.XPATH,'//*[@id="goods-info"]/div[4]/button[1]')

        #货到付款
        self.btn_select_buy_2=(By.XPATH,'//*[@id="checkout"]/div[2]/div[2]/div[2]/div[2]/ul/li[2]')
        #在线支付
        self.btn_select_buy_1=(By.XPATH,'//*[@id="checkout"]/div[2]/div[2]/div[2]/div[2]/ul/li[1]')
        #送达时间
        self.btn_time_any=(By.XPATH,'//*[@id="checkout"]/div[2]/div[2]/div[4]/div[2]/div[1]')
        self.btn_time_work = (By.XPATH, '//*[@id="checkout"]/div[2]/div[2]/div[4]/div[2]/div[2]')
        self.btn_time_free = (By.XPATH, '//*[@id="checkout"]/div[2]/div[2]/div[4]/div[2]/div[3]')

        #提交
        self.btn_submit=(By.XPATH,'//*[@id="checkout"]/div[2]/div[3]/div[3]/a')


    def buy(self):
        self.base_click(self.production_click)
        self.switch_to_latest_window()
        time.sleep(5)
        self.base_click(self.btn_buy)
        self.base_click(self.btn_select_buy_2)
        self.base_click(self.btn_time_any)
        self.base_click(self.btn_submit)

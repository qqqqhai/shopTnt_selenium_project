from selenium.webdriver.common.by import By

from base.base import BasePage
from config import BASE_URL_SELLER


class PageAddProduction(BasePage):
    def __init__(self,driver):
        """登录"""

        super().__init__(driver)
        self.select_title = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span')
        self.select_title_list1 =(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/a[1]/li/span')
        self.select_title_list1_btn1 =(By.XPATH,'//*[@id="app"]/div/div[3]/section/div/div[1]/div[1]/div/div[1]/button[1]')

        self.select_class1 =(By.XPATH,'//*[@id="app"]/div/div[3]/section/div/div[2]/div/ul/li[1]')

        self.select_class2 =(By.XPATH,'//*[@id="app"]/div/div[3]/section/div/div[2]/div/ul[2]/li[1]')

        self.select_class3_1=(By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[2]/div/ul[3]/li[1]')
        self.select_class3_2 = (By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[2]/div/ul[3]/li[2]')
        self.select_class3_3 = (By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[2]/div/ul[3]/li[3]')

        self.goto_next = (By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[4]/div/button')

        self.select_name = (By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[3]/form/div[2]/div/div[1]/div/div/input')
        self.select_num = (By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[3]/form/div[2]/div/div[2]/div/div/input')
        self.select_price1 = (By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[3]/form/div[2]/div/div[4]/div/div/input')
        self.select_price2 = (By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[3]/form/div[2]/div/div[5]/div/div/input')
        self.select_weight = (By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[3]/form/div[2]/div/div[6]/div/div/input')
        self.select_img = (By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[3]/form/div[2]/div/div[8]/div/div[1]/div[2]/div[1]')

        self.select_img_what=(By.XPATH,'/html/body/div[3]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]')
        self.select_img_btn=(By.XPATH,'/html/body/div[3]/div/div[3]/span/button[2]/span')

        self.select_btn_add=(By.XPATH,'//*[@id="app"]/div/div[3]/section/div/div[4]/div/button[3]')

        self.alter_success=(By.XPATH,'/html/body/div[3]')

    def open_url(self):
        self.driver.get(BASE_URL_SELLER)
    def add_production(self,add_class,select_name,select_num,select_price1,select_price2,select_weight):
        self.base_click(self.select_title)
        self.base_click(self.select_title_list1)
        self.base_click(self.select_title_list1_btn1)

        self.base_click(self.select_class1)
        self.base_click(self.select_class2)
        if add_class==1:
            self.base_click(self.select_class3_1)
        elif add_class==2:
            self.base_click(self.select_class3_2)
        else:
            self.base_click(self.select_class3_3)
        self.base_click(self.goto_next)

        self.base_input(self.select_name,select_name)
        self.base_input(self.select_num,select_num)
        self.base_input(self.select_price1,select_price1)
        self.base_input(self.select_price2,select_price2)
        self.base_input(self.select_weight, select_weight)
        self.base_click(self.select_img)
        self.base_click(self.select_img_what)
        self.base_click(self.select_img_btn)
        self.base_click(self.select_btn_add)


    def jug_add_msg(self):
        try:
            return self.fd_element(self.alter_success).text
        except:
            return None

if __name__=='__main__':
    pass
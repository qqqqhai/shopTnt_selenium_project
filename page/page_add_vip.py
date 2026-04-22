from selenium.webdriver.common.by import By

from base.base import BasePage
from config import  BASE_URL1
from page.page_login import PageLogin
from tools import DriverTools


class PageAddVip(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.select_vip = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/div')
        self.select_vip_list =(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/a[1]/li')
        self.select_add =(By.XPATH,'//*[@id="app"]/div/div[3]/section/div/div[1]/div[1]/div/div[1]/button')

        self.vip_name =(By.XPATH,'//*[@id="app"]/div/div[3]/section/div/div[2]/div/div[2]/form/div[1]/div/div/input')
        self.vip_sex_nan =(By.XPATH,'//*[@id="app"]/div/div[3]/section/div/div[2]/div/div[2]/form/div[2]/div/label[1]/span[1]/span')
        self.vip_sex_nv=(By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[2]/div/div[2]/form/div[2]/div/label[2]/span[1]/span')
        self.vip_pwd=(By.XPATH,'//*[@id="app"]/div/div[3]/section/div/div[2]/div/div[2]/form/div[3]/div/div/input')
        self.vip_en_pwd=(By.XPATH,'//*[@id="app"]/div/div[3]/section/div/div[2]/div/div[2]/form/div[4]/div/div/input')
        self.vip_phone=(By.XPATH,'//*[@id="app"]/div/div[3]/section/div/div[2]/div/div[2]/form/div[5]/div/div/input')
        self.btn=(By.XPATH,'//*[@id="app"]/div/div[3]/section/div/div[2]/div/div[3]/div/button[2]/span')

        #错误信息
        self.err_name=(By.XPATH,'//*[@id="app"]/div/div[3]/section/div/div[2]/div/div[2]/form/div[1]/div/div[2]')
        self.err_sex = (By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[2]/div/div[2]/form/div[2]/div/div')
        self.err_pwd = (By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[2]/div/div[2]/form/div[3]/div/div[2]')
        self.err_en_pwd = (By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[2]/div/div[2]/form/div[4]/div/div[2]')
        self.err_vip_phone = (By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[2]/div/div[2]/form/div[5]/div/div[2]')

        #登录信息
        self.add_msg=(By.CSS_SELECTOR, 'div[role="alert"].el-message p.el-message__content')
    def open_url(self):
        self.driver.get(BASE_URL1)
    def add_vip(self,vip_name,vip_en_pwd,vip_pwd,vip_phone,sex):
        self.base_click(self.select_vip)
        self.base_click(self.select_vip_list)
        self.base_click(self.select_add)
        self.base_input(self.vip_name,vip_name)
        self.base_input(self.vip_pwd,vip_pwd)
        self.base_input(self.vip_en_pwd,vip_en_pwd)
        self.base_input(self.vip_phone,vip_phone)

        if sex == "男":
            self.base_click(self.vip_sex_nan)
        else:
            self.base_click(self.vip_sex_nv)
        self.base_click(self.btn)

    def jug_add_vip(self,a):
        res = []
        # 定义辅助函数：尝试获取文本，如果找不到（没报错）则返回 None
        def safe_get(locator):
            try:
                return self.get_text(locator)
            except Exception:
                return None
        # 0: 用户名, 1: 性别, 2: 密码, 3: 确认密码, 4: 手机号
        res.append(safe_get(self.err_name))
        res.append(safe_get(self.err_sex))
        res.append(safe_get(self.err_pwd))
        res.append(safe_get(self.err_en_pwd))
        res.append(safe_get(self.err_vip_phone))

        # JSON 里的 a 是字符串，必须转为整数才能作为索引
        index = int(a)

        # 返回指定位置的那个错误信息
        # 如果 index 越界，这里可能会报错，请确保 JSON 里的 a 不超过 4
        return res[index]
    def jug_add_msg(self):
        try:
            return self.fd_element(self.add_msg).text
        except:
            return None


if __name__ =="__main__":
    PageAddVip(driver=DriverTools.get_driver()).get_url()
    PageLogin(driver=DriverTools.get_driver()).login("admin","111111","1111")


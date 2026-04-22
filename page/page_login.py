from selenium.webdriver.common.by import By

from base.base import BasePage
from config import BASE_URL
from tools import DriverTools


class PageLogin(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

        self.user_id = (By.XPATH, "//*[@id='app']/div/div[2]/form/div[1]/div/div[1]/input")
        self.password = (By.XPATH, '//*[@id="app"]/div/div[2]/form/div[2]/div/div/input')
        self.img = (By.XPATH, '//*[@id="app"]/div/div[2]/form/div[3]/div/div/img')
        self.img_pwd = (By.XPATH, '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div/input')
        self.btn_login = (By.XPATH, '//*[@id="app"]/div/div[2]/form/div[4]/div/button')
        #成功标志
        self.success_topic=(By.XPATH,'//*[@id="app"]/div/div[3]/div/ul/div[1]/div/div[2]/div/a')
        #提示词弹框
        self.error_msg = (By.XPATH, "//div[contains(@class, 'el-message--error')]//p[@class='el-message__content']")

    def open_url(self):
        self.driver.get(BASE_URL)
    def login(self,user_name,password,img_pwd):
        self.base_input(self.user_id,user_name)
        self.base_input(self.password, password)
        self.base_click(self.img_pwd)
        self.base_input(self.img_pwd,img_pwd)
        self.base_click(self.btn_login)



class jud_handles(PageLogin):
    def __init__(self,driver):
        super().__init__(driver)
        #是否跳转成功
    def jud_handles_jump(self):

            if self.fd_element(self.success_topic):
                return True
            else:
                return False
    #是否有错误提示
    def alter_jud(self):
        return self.fd_element(self.error_msg).text

if __name__=='__main__':
    PageLogin().get_url()
    PageLogin().login("admin","111111","1111")
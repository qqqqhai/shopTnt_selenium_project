from selenium.webdriver.common.by import By

from base.base import BasePage


class PageLoginCustom(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        #点击登录
        self.btn_login=(By.XPATH,'//*[@id="shortcut"]/div/div/span[2]/a[1]')

        self.pho_input = (By.XPATH, '//*[@id="mobile"]')
        self.img_input = (By.XPATH, '//*[@id="validcode-mobile"]')
        self.get_email = (By.XPATH, '//*[@id="login"]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div[3]/button')
        self.email_input = (By.XPATH, '//*[@id="sms-code"]')

        self.btn_login_custom = (By.XPATH, '//*[@id="login"]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/button')

        self.login_success =(By.XPATH,'//*[@id="shortcut"]/div/div/ul/li/div[1]/a')

        self.login_err =(By.CLASS_NAME,'el-message__content')
    def login_custom(self,phone,img,email):
        self.base_click(self.btn_login)
        self.base_input(self.pho_input,phone)
        self.base_input(self.img_input,img)
        self.base_click(self.get_email)
        self.base_input(self.email_input,email)
        self.base_click(self.btn_login_custom)

    def jug_login_success(self):
        try:
            return self.fd_element(self.login_success).text
        except:
            return None

    def jug_login_err(self):
        try:
            return self.fd_element(self.login_err).text
        except:
            return None

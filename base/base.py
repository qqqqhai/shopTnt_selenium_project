from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from tools import DriverTools, GetLog
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    #打开网址
    def __init__(self,driver,timeout=3):
        self.driver = driver
        self.default_timeout=timeout
    def get_url(self):
        self.driver.get("https://manager-bbc.shoptnt.cn")
    #元素显示等待
    def fd_element(self, loc):
        #try:
            return  WebDriverWait(self.driver, self.default_timeout, 1).until(EC.visibility_of_element_located(loc))
        #except Exception as e:
            # GetLog.get_log().error(f"元素定位超时，定位信息:{loc},详细错误:{e}")
            #raise

    #点击
    def base_click(self,loc):
        self.fd_element(loc).click()
    #输入
    def base_input(self,loc,text):
        ele_user_id = self.fd_element(loc)
        ele_user_id.clear()
        ele_user_id.send_keys(text)
    #获取文本
    def get_text(self,loc):
        try:
            if self.fd_element(loc):
                return self.fd_element(loc).text
        except TimeoutException:
            # 如果超时没找到，说明没有这个错误提示，返回 None 或空字符串
            return None
    #页面滚动到底部
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

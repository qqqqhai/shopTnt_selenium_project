from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
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
        try:
            return  WebDriverWait(self.driver, self.default_timeout, 1).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            GetLog.get_log().error(f"元素定位超时，定位信息:{loc},详细错误:{e}")
            raise
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
    #切换新窗口
    def switch_to_latest_window(self, original_handle, timeout: int = 10):
        try:
            # 1. 显式等待：等待新窗口出现（句柄列表中出现不同于原句柄的新句柄）
            WebDriverWait(self.driver, timeout).until(
                lambda d: any(handle != original_handle for handle in d.window_handles)
            )
            # 2. 获取所有窗口句柄，筛选出最新的那个
            all_handles = self.driver.window_handles
            # 取出所有不等于原句柄的句柄，取最后一个（最新打开的）
            new_handles = [handle for handle in all_handles if handle != original_handle]
            latest_handle = new_handles[-1]

            # 3. 执行切换
            self.driver.switch_to.window(latest_handle)

            # 4. 可选：等待新页面加载完成（比等待 title 更靠谱）
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )

            print(f"✅ 切换窗口成功！原句柄: {original_handle[-6:]}... -> 新句柄: {latest_handle[-6:]}...")

        except TimeoutException:
            print(f"❌ 切换窗口超时！原句柄: {original_handle}, 当前所有句柄: {self.driver.window_handles}")
            raise  # 重新抛出异常，让 pytest 标记用例失败
    #鼠标悬停
    def base_hover(self, loc):
        # 1. 获取元素 (直接复用你写好的 fd_element，自带显式等待，防止元素未加载)
        element = self.fd_element(loc)
        # 2. 执行悬停动作
        ActionChains(self.driver).move_to_element(element).perform()
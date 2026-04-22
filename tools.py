import json
import time
import logging
from logging import  handlers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import PATH


class DriverTools:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            Path = r"D:\Python313\chromedriver.exe"
            ser = Service(executable_path=Path)
            cls.driver = webdriver.Chrome(service=ser)

            cls.driver.maximize_window()

        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            time.sleep(3)
            cls.driver.quit()
            cls.driver = None

def read_json(file_name):
    data =[]
    file_path = PATH +"/data/" +file_name
    with open(file_path,mode='r',encoding='utf-8')as f:
        tmp = json.load(f)
        for i in tmp:
            a=tuple(i.values())
            data.append(a)
        return  data

class GetLog:
    # 私有类变量，存储单例日志器
    __log = None
    @classmethod
    def get_log(cls):
        if cls.__log is None:
            # 1. 获取日志器并设置级别
            cls.__log = logging.getLogger()  # 根日志器（也可指定名称：logging.getLogger("project_log")）
            cls.__log.setLevel(logging.INFO)  # 日志级别：INFO及以上
            filename = PATH +"/log/" + 'web.log'
            tf = logging.handlers.TimedRotatingFileHandler(
                filename=filename,
                when="midnight",
                interval=1,
                backupCount=3,
                encoding="utf-8"
            )
            fmt = "%(asctime)s %(levelname)s [%(filename)s%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            tf.setFormatter(fm)
            cls.__log.addHandler(tf)

        # 返回单例日志器
        return cls.__log

if __name__ == '__main__':
    # DriverTools.get_driver().get('https://manager-bbc.shoptnt.cn')
    # DriverTools.quit_driver()
    print(read_json("login_data.json"))

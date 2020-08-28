# 定义获取浏览器驱动的工具类
import json
import time
from lib2to3.pgen2 import driver

import allure
import appium.webdriver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

"""
封装小技巧
1.定义方法
2.将其中的一份实现拷贝方法当中
3.再修改报错的部分以及调整
4.在修改调用的地方，通过方法调用来代替原来的代码
"""


class DriverUtils:
    # 自媒体驱动对象私有属性
    __driver_mp = None
    # 后台管理系统驱动对象私有属性
    __driver_mis = None
    # app驱动系统驱动对象私有属性
    __driver_app = None
    __mp_key = True
    __mis_key =True

    # 获取已经初始化好莱客的浏览器驱动对象的方法
    # 为了方便调用，定义成类级别的方法
    @classmethod
    def driver_get_mp(cls):
        # 为了防止脚本多次调用获取浏览器驱动对象的方法产生多个浏览器窗口
        # 添加私有变量__driver来储存浏览器驱动对象，并且判断
        if cls.__driver_mp is None:
            # 创建浏览器驱动对象---->打开浏览器
            cls.__driver_mp = webdriver.Chrome()
            cls.__driver_mp.maximize_window()
            cls.__driver_mp.implicitly_wait(30)
            cls.__driver_mp.get("http://ttmp.research.itcast.cn/")
        # 返回窗口最大化以及隐式等待的浏览器驱动对象
        return cls.__driver_mp

    # 自媒体——关闭浏览器驱动对象
    @classmethod
    def driver_mp_quit(cls):
        if cls.__driver_mp is not None and cls.__mp_key:
            time.sleep(2)
            cls.__driver_mp.quit()
            cls.__driver_mp = None

    # 修改mp自媒体关闭浏览器驱动的开关方式
    @classmethod
    def change_mp_key(cls, key):
        cls.__mp_key = key



    @classmethod
    def driver_get_mis(cls):
        # 为了防止脚本多次调用获取浏览器驱动对象的方法产生多个浏览器窗口
        # 添加私有变量__driver来储存浏览器驱动对象，并且判断
        if cls.__driver_mis is None:
            # 创建浏览器驱动对象---->打开浏览器
            cls.__driver_mis = webdriver.Chrome()
            cls.__driver_mis.maximize_window()
            cls.__driver_mis.implicitly_wait(30)
            cls.__driver_mis.get("http://ttmis.research.itcast.cn/")
        # 返回窗口最大化以及隐式等待的浏览器驱动对象
        return cls.__driver_mis

    @classmethod
    def change_mis_key(cls, key):
        cls.__mis_key = key

    # 封装获取元素的信息的公用方法

    # 后台管理系统——关闭浏览器驱动对象
    @classmethod
    def driver_mis_quit(cls):
        if cls.__driver_mis is not None  and cls.__mis_key:
            time.sleep(2)
            cls.__driver_mis.quit()
            cls.__driver_mis = None

    # 封装获取元素的信息的公用方法
    # app系统获取驱动对象得方法
    @classmethod
    def get_app_driver(cls):
        if cls.__driver_app is None:
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '7.1.2'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = 'com.itcast.toutiaoApp'
            desired_caps['appActivity'] = '.MainActivity'
            desired_caps['noReset'] = True
            cls.__driver_app = appium.webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            cls.__driver_app.implicitly_wait(30)
        return cls.__driver_app

        # 后台管理系统-关闭浏览器驱动的方法

    @classmethod
    def quit_app_driver(cls):
        # 为了保障代码的健壮性,防止异常报错,先判断当前是否有浏览器驱动对象是否存在
        if cls.__driver_app is not None:
            # 关闭浏览器
            time.sleep(4)
            # quit()只是关闭整个浏览器但是并不会将__driver的值设置为空,而是保留一串缓存字符串
            cls.__driver_app.quit()
            # 将__driver设置为空
            cls.__driver_app = None
    # 根据文本判断元素是否存在的公用方法


def is_element_exist(driver, text):
    str_xpath = "//*[contains(text(),'{}')]".format(text)
    try:
        is_element = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(str_xpath))
        return is_element
    except Exception as e:
        NoSuchElementException("找不到文本{}的元素对象".format(text))

def is_el_by_attribute(driver, attr_name,attr_value):
    str_xpath = "//*[contains(@{},'{}')]".format(attr_name,attr_name)
    try:
        is_element = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(str_xpath))
        return is_element
    except Exception as e:
        NoSuchElementException("找不到文本{}的元素对象".format(attr_name,attr_name))

    # 封装公共的下拉选择框方法


def check_channel_option(driver, channel_name, option_name):
    # 定位下拉框
    str_xpath = "//*[contains(@placeholder,'{}')]".format(channel_name)
    # 点击频选择框的元素对象
    driver.find_element_by_xpath(str_xpath).click()

    # 获取所有选项的频道名称
    channel_option = driver.find_elements_by_css_selector(".el-select-dropdown__item span")
    is_suc = False
    # 遍历所有选项
    for option_element in channel_option:
        if option_element.text == option_name:
            option_element.click()
            is_suc = True
            break
        else:
            action = ActionChains(driver)
            action.move_to_element(option_element).send_keys(Keys.DOWN).perform()
            is_suc = False
    if is_suc is False:
        NoSuchElementException("cann`t find name is {} channel option".format(channel_name))

# 封装读取数据并组装成parameteriz所要求数据格式函数
def get_case_data(file_path):
    # 定义一个空列表
    test_data = []
    # 1.读取数据文件中的数据
    with open(file=file_path, encoding="utf-8")as f:
        str_dict = json.load(f)
        # 2.遍历所有的键值
        for i in str_dict.values():
            # 3.一次性获取键值所有键值,并且把返回的结果直接追加到空列表中
            test_data.append(list(i.values()))
            print(test_data)
    return test_data
def get_allure_pne(driver,filename):
    allure.attach(driver.get_screenshot_as_png(),filename,allure.attachment_type.PNG)
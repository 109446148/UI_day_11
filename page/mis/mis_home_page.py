# 后台管理系统 ---首页
# 简单的方式来封装po，注意一般面试的时候不要用这种方式来回答
# 但是实际工作中的时候如果没有强行要求，则可以使用下面的方式来编写代码


# 定义页面对象类 - --继承base里面的公用方法
import time

from selenium.webdriver.common.by import By

from base.mis_base.base_page import BasePage, BaseHandle


class MisHomePage(BasePage, BaseHandle):
    # 定义实例属性 - ---》每个元素对象就是页面对象的实例属性
    def __init__(self):
        super().__init__()
        # 定义信息管理菜单栏
        self.info_manage_tab = (By.XPATH, "//*[contains(text(),'信息管理')]")

        # 定义内容管理菜单栏
        self.context_manage_tab = (By.XPATH, "//*[contains(text(),'内容审核')]")

    # 定义实例方法 - --->实例方法对应的是测试步骤中以连续性动作
    # 定义跳转内容审核页面的实例方法
    def to_ari_mispage(self):
        # 点击信息管理菜单栏
        self.find_elt(self.info_manage_tab).click()
        time.sleep(3)
        # 点击内容审核菜单栏
        self.find_elt(self.context_manage_tab).click()

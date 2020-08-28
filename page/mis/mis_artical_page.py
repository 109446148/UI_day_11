# 对象库层
# 创建类
import time

from selenium.webdriver.common.by import By

from base.mis_base.base_page import BasePage, BaseHandle
from utils import check_channel_option, DriverUtils


class MisAtcalPage(BasePage):
    def __init__(self):
        super().__init__()
        # 文章标题搜索输入框
        self.mis_title = (By.CSS_SELECTOR, "[placeholder*='文章名称']")
        # 选择频道
        self.mis_channel = (By.CSS_SELECTOR, "[placeholder='请输入: 频道']")
        # 查询按钮
        self.mis_query = (By.CSS_SELECTOR, ".find")
        # 通过按钮
        self.mis_pass = (By.XPATH, "//*[text()='通过']")
        # 驳回按钮
        self.mis_reject = (By.XPATH, "//*[text()='驳回']")
        # 通过/驳回确认按钮
        self.mis_con_rej_btn = (By.CSS_SELECTOR, ".el-button--primary")
        #

    # 找到文章标题搜索输入
    def find_mis_title(self):
        return self.find_elt(self.mis_title)
        # 找到选择频道

    def find_mis_channel(self):
        return self.find_elt(self.mis_channel)
        # 找到查询按钮

    def find_mis_query(self):
        return self.find_elt(self.mis_query)
        # 找到通过按钮

    def find_mis_pass(self):
        return self.find_elt(self.mis_pass)
        # 找到驳回按钮

    def find_mis_reject(self):
        return self.find_elt(self.mis_reject)
        # 找到通过/驳回确认按钮

    def find_con_rej_btn(self):
        return self.find_elt(self.mis_con_rej_btn)


# 创建操作类
class MisAtcalHandle(BaseHandle):
    # 	实例化对象库层的方法
    def __init__(self):
        self.mis_page = MisAtcalPage()

    # 	--文章标题搜索输入框输入--调用base文件的方法
    def input_mis_title(self, ari_title):
        element = self.mis_page.find_mis_title()
        self.input_text(element, ari_title)
        # 	--选择文章状态

    def check_status(self, ari_status):
        check_channel_option(DriverUtils.driver_get_mis(), "请选择状态", ari_status)

    # 	--查询按钮点击
    def click_queryt(self):
        self.mis_page.find_mis_query().click()

    # 	--通过按钮点击
    def click_pass(self):
        self.mis_page.find_mis_pass().click()

    # 	--驳回按钮点击
    def click_regic(self):
        self.mis_page.find_mis_reject().click()

    # 	--通过/驳回确认按钮点击
    def click_confim(self):
        self.mis_page.find_con_rej_btn().click()


class MisAtcalProxy:
    def __init__(self):
        # 实例化对象
        self.mis_handle = MisAtcalHandle()
        # 业务层--》连续调用多个操作方法形成操作步骤
        # 审核通过测试用例

    def test_pass(self, ari_title):
        # 1.输入搜索的文章名称
        self.mis_handle.input_mis_title(ari_title)
        # 2.选择文章状态
        self.mis_handle.check_status("待审核")
        # 3.点击查询按钮
        self.mis_handle.click_queryt()
        time.sleep(3)
        # 4.点击通过按钮
        self.mis_handle.click_pass()
        # 5.点击确认按钮
        self.mis_handle.click_confim()
        time.sleep(3)
        # 6.选择文章状态
        self.mis_handle.check_status("审核通过")
        # 7.点击查询按钮
        self.mis_handle.click_queryt()
        time.sleep(3)

    def test_regic(self, ari_tltle):
        # 审核驳回测试用例
        # 输入搜索的文章名称
        # self.mis_handle.input_mis_title(ari_tltle)
        # 选择文章状态
        self.mis_handle.check_status("待审核")
        # 点击查询按钮
        self.mis_handle.click_queryt()
        time.sleep(3)
        # 点击驳回按钮
        self.mis_handle.click_regic()
        # 点击确认按钮
        self.mis_handle.click_confim()
        time.sleep(3)
        # 6.选择文章状态
        self.mis_handle.check_status("审核失败")
        # 7.点击查询按钮
        self.mis_handle.click_queryt()
        time.sleep(3)
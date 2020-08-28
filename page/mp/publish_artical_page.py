"""发表文章页面"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.mp_base.base_page import BasePage, BaseHandle
from utils import DriverUtils, check_channel_option


class PubAriPage(BasePage):
    # 使用属性定义所有要操作的元素定位方式以及表达式
    # 使用实例方法找到所有要用到元素
    def __init__(self):
        super().__init__()
        # 标题
        self.ari_title = (By.CSS_SELECTOR, "[placeholder='文章名称']")
        # iframe
        self.ari_iframe = (By.CSS_SELECTOR, "#publishTinymce_ifr")
        # 内容
        self.ari_context = (By.CSS_SELECTOR, "body")
        # 封面
        self.ari_cover = (By.XPATH, "//*[text()='自动']")
        # 频道选择框
        self.channel = (By.CSS_SELECTOR, "[placeholder='请选择']")
        # 频道选项
        self.channel_option = (By.XPATH, "//*[text()='开发者资讯']")
        # 发表
        self.pub_btn = (By.XPATH, "//*[text()='发表']")

    # 找标题
    def find_ari_title(self):
        return self.find_elt(self.ari_title)

    def find_ari_iframe(self):
        return self.find_elt(self.ari_iframe)

    def find_ari_context(self):
        return self.find_elt(self.ari_context)

    def find_ari_cover(self):
        return self.find_elt(self.ari_cover)

    def find_channel(self):
        return self.find_elt(self.channel)

    def find_cannel_option(self):
        return self.find_elt(self.channel_option)

    def find_pub_btn(self):
        return self.find_elt(self.pub_btn)


class PubAriHandle(BaseHandle):
    def __init__(self):
        self.pub_ari_page = PubAriPage()

    def input_ari_title(self, title):
        self.input_text(self.pub_ari_page.find_ari_title(), title)

    def input_ari_conten(self, context):
        DriverUtils.driver_get_mp().switch_to.frame(self.pub_ari_page.find_ari_iframe())
        self.input_text(self.pub_ari_page.find_ari_context(), context)
        DriverUtils.driver_get_mp().switch_to.default_content()

    def check_ari_cover(self):
        self.pub_ari_page.find_ari_cover().click()

    def check_ari_channel(self, channel_name):
        # 调用工具类的公用下拉框方法

        check_channel_option(DriverUtils.driver_get_mp(),"请选择",channel_name)
    def click_pub_ari_bth(self):
        self.pub_ari_page.find_pub_btn().click()


class PubAriProxy:
    def __init__(self):
        self.pub_handle = PubAriHandle()

    def test_pub_artcal(self, tltle, context, channel_name):
        # 输入标题
        self.pub_handle.input_ari_title(tltle)
        # 输入内容
        self.pub_handle.input_ari_conten(context)
        # 选择封面
        self.pub_handle.check_ari_cover()
        # 选择频道
        self.pub_handle.check_ari_channel(channel_name)
        # 点击发表
        self.pub_handle.click_pub_ari_bth()

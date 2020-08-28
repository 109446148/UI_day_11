import time

import pytest

import config
from page.mis.login_mis_page import MisLoginProxy
from page.mis.mis_artical_page import MisAtcalPage, MisAtcalProxy
from page.mis.mis_home_page import MisHomePage
from utils import DriverUtils, is_element_exist

@pytest.mark.run(order=103)
class TestAritcleMana:
    # 类级别的初始化方法
    def setup_class(self):
        # 打开浏览器
        self.driver = DriverUtils.driver_get_mis()
        # 创建登录页面业务对象
        self.login_page = MisLoginProxy()
        # 创建首页类对象
        self.home_page = MisHomePage()
        # 创建文章审核页面对象
        self.ad_page = MisAtcalProxy()

    # def setup(self):
    #     time.sleep(3)
    #     self.driver.get("http://ttmis.research.itcast.cn/#/home")

    # 登录
    # @pytest.mark.run(order=1)
    # def test_login(self):
    #     self.login_page.test_mis_login("testid", "testpwd123")


    def test_aduit_pass(self):
        ari_title = config.PUB_ARITCAL_TITLE
        print("审核文章的标题为：",ari_title)
        # 调用进入审核页面的业务方法
        self.home_page.to_ari_mispage()
        # 调用审核文章的业务方法
        self.ad_page.test_pass(ari_title)
        # 断言
        assert is_element_exist(self.driver, "驳回")

    # @pytest.mark.run(order=3)
    # def test_aduit_regic(self, ari_title):
    #     ari_title = "test-20190424-001"
    #     self.home_page.to_ari_mispage()
    #     self.ad_page.test_regic(ari_title)
    #     assert is_element_exist(self.driver, "查看")

    def teardown_class(self):
        DriverUtils.driver_mis_quit()

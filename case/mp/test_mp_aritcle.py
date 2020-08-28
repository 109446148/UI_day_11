import time

import pytest

import config
from page.mp.home_page import HomeProxy
from page.mp.login_page import LoginProxy
from page.mp.publish_artical_page import PubAriProxy
from utils import DriverUtils, is_element_exist, get_case_data, get_allure_pne


@pytest.mark.run(order=3)
class TestPubAritcle:
    def setup_class(self):
        # 打开新浏览器
        self.driver = DriverUtils.driver_get_mp()
        # 创建首页业务层对象
        self.home_proxy = HomeProxy()
        # 创建发布文章业务成的对象
        self.pub_ari_proxy = PubAriProxy()
        # 创建登录页面的业务层对象
        # self.login_proxy = LoginProxy()
    def setup_method(self):
        self.driver.get("http://ttmp.research.itcast.cn/")

    # 定义测试方法
    @pytest.mark.parametrize(("title_ari", "context_ari", "channel_ari", "expect"),
                             get_case_data("./data/mp/test_pub_ari_data.json"))
    def test_pub_ari(self, title_ari, context_ari, channel_ari, expect):
        # 组织测试数据
        config.PUB_ARITCAL_TITLE = title_ari.format(time.strftime("%H%M%S"))
        # 执行测试步骤
        self.home_proxy.to_pub_ari_page()
        self.pub_ari_proxy.test_pub_artcal(config.PUB_ARITCAL_TITLE, context_ari, channel_ari)
        get_allure_pne(self.driver,"发布文章")
        # 断言
        assert is_element_exist(self.driver, expect)

    def teardown_class(self):
        DriverUtils.driver_mp_quit()

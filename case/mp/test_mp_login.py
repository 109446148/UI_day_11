# 1.定义测试类
import time

import allure
import pytest

from page.mp.login_page import LoginProxy

from utils import DriverUtils, is_element_exist

@pytest.mark.run(order=2)
class TestMpLlogin:
    # 2.定义初始化方法
    def setup_class(self):
        #     2.1获取驱动对象
        self.driver = DriverUtils.driver_get_mp()
        # 2.2创建好所需要的的调用业务方法所在的类的对象
        self.login_proxy = LoginProxy()

    #
    #     3定义测试方法
    @allure.severity(allure.severity_level.MINOR)
    def test_mp_login(self):
        username = "13911111111"
        code = "246810"
        #         3.1定义测试数据
        self.login_proxy.test_mp_login(username, code)
        #         3.2调用业务方法形成完整的业务操作
        time.sleep(1)
        #         3.3断言
        assert is_element_exist(self.driver, "江苏传智播客")

    def teardown_class(self):
        time.sleep(3)
        DriverUtils.driver_mp_quit()

import time

import pytest

from page.mis.login_mis_page import MisLoginProxy

from utils import DriverUtils, is_element_exist

@pytest.mark.run(order=102)
class TestMisLogin:
    # 定义初始化方法
    def setup_class(self):
        #     获取驱动对象
        self.driver = DriverUtils.driver_get_mis()
        #     创建好需要调用业务方法的所在类的对象
        self.login_proxy = MisLoginProxy()

    # 定义测试方法
    def test_mis_login(self):
        username = "testid"
        password = "testpwd123"
        self.login_proxy.test_mis_login(username, password)
        time.sleep(2)
        assert is_element_exist(self.driver, "黑马头条后台管理系统")

    def teardown_class(self):
        time.sleep(3)
        DriverUtils.driver_mis_quit()

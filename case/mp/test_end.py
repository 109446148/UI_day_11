import pytest

from utils import DriverUtils


@pytest.mark.run(order=99)
class TestEnd:
    def test_end(self):
        # 将关闭浏览区的驱动开关打开
        DriverUtils.change_mp_key(True)
        # 主动调用一次关闭浏览器的驱动方法
        DriverUtils.driver_mp_quit()

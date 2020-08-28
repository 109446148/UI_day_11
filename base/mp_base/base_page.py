# 对象库中——基类，把定位元素的方法定义在基类中
# 定义对象层的基类
from utils import DriverUtils


class BasePage:
    def __init__(self):
        self.driver = DriverUtils.driver_get_mp()

    # 公用的元素定位方法
    def find_elt(self, location):
        return self.driver.find_element(*location)


# 定义操作层的基类

class BaseHandle:

    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)


class BaseTools:
    # 对于复杂selenium或者是都appium所提供的挨批自己可以进行一个二次封装
    def to_window(self, n):
        handles = DriverUtils.driver_get_mp().window_handles
        DriverUtils.driver_get_mp().switch_to(handles[n])

# 对象库层--->管理维护页面的所有元素
from selenium.webdriver.common.by import By

from base.mis_base.base_page import BasePage, BaseHandle
from utils import DriverUtils


class MisLoginPage(BasePage):
    # 初始化对象
    def __init__(self):
        super().__init__()
        # 定位输入框
        self.username = (By.NAME, "username")
        # 定位密码
        self.password = (By.NAME, "password")
        # 定位登录按钮
        self.login_btn = (By.ID, "inp1")

    # 实例化方法
    #找输入框的方法
    def mis_username(self):
        return self.find_elt(self.username)
    # 找密码框的方法
    def mis_password(self):
        return self.find_elt(self.password)
    # 找登录按钮的方法
    def mis_login_btn(self):
        return self.find_elt(self.login_btn)


# 操作层---->专门封装元素对象的操作方法
class MisLoginHandle(BaseHandle):
    # 实例化对象库层的方法
    def __init__(self):
        self.mis_pag_login = MisLoginPage()

    # --创建用户名输入的方法 - -调用base文件的方法
    def input_username(self, username):
        self.input_text(self.mis_pag_login.mis_username(), username)

    # --创建密码输入的方法 - -调用base文件的方法
    def input_password(self, password):
        self.input_text(self.mis_pag_login.mis_password(), password)
    # --创建登录按钮方法
    def click_login_btn(self):
    # 需要先删除按钮元素对象disabled属性
        js_str = "document.getElementById('inp1').removeAttribute('disabled')"
        DriverUtils.driver_get_mis().execute_script(js_str)
    # 点击登录
        self.mis_pag_login.mis_login_btn().click()

# 业务层---->连续调用多个操作层的方法形成手工测试用例的步骤
class MisLoginProxy:
    # 创建登录方法 - --》调用操作层的方法
    def __init__(self):
        # 先实例操作层的对象
        self.mis_login_handle =MisLoginHandle()
    def test_mis_login(self,username,password):
        # 输入用户名 - -调用操作层输入用户名的方法
        self.mis_login_handle.input_username(username)
        # 输入密码 - --调用操作层输入密码的方法
        self.mis_login_handle.input_password(password)
        # 点击登录 - --调用操作层登录方法
        self.mis_login_handle.click_login_btn()



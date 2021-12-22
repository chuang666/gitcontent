from selenium.webdriver.common.by import By
import unittest
from CommonUtils import CommonUtils


class TestPwdLogin(unittest.TestCase):
    cu = CommonUtils()
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pwd_login(self):

        self.cu.login_page()
        # 验证登录成功
        result = self.cu.get_quit_element()
        self.assertEqual(result, "退出")

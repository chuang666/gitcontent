from selenium.webdriver.common.by import By
import unittest
from CommonUtils import CommonUtils


class TestEnterTenant(unittest.TestCase):
    cu = CommonUtils()
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_enter_tenant_success(self):

        self.cu.login_page()
        self.cu.enter_econfig()
        page_tenant_name,tenant_admin,tenant_basic_info= self.cu.get_enter_success_element()
        # 校验成功进入租户
        self.assertEqual(page_tenant_name,"湖南健朗药业有限责任公司")
        self.assertEqual(tenant_admin,"管理员")
        self.assertEqual(tenant_basic_info,"基本信息")

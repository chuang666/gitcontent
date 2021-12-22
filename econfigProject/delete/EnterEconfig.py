from selenium import webdriver
from selenium.webdriver.common.by import By
from Constants import *
import time, unittest


class SelectEconfig(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pwd_login(self):
        # 打开浏览器
        global driver
        driver_path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.maximize_window()
        # 进入登录页面
        driver.get(TESTURL)
        # driver.implicitly_wait(5)
        # 选择密码登录
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@class='toggle-login-text active']").click()
        # 输入用户名、密码
        driver.find_element(By.ID, "username").send_keys(USERNAME)
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys(PWD)
        time.sleep(1)
        # 点击登录
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        # 点击econfig
        iframe = driver.find_element(By.XPATH, "//div/iframe")
        driver.switch_to.frame(iframe)  # 跳出框架
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@class='icon-img']").click()
        time.sleep(2)
        #选择租户
        driver.find_element(By.XPATH, "//div[@title='湖南健朗药业有限责任公司']").click()
        time.sleep(2)
        #验证进入租户页面
        a_list = driver.find_element(By.XPATH, "//*[@class='tenant_name']")
        page_tenant_name = a_list.find_element(By.XPATH, "//*[@title='湖南健朗药业有限责任公司']").get_attribute("title")
        print(page_tenant_name)
        tenant_admin = driver.find_element(By.LINK_TEXT, "管理员").text
        print(tenant_admin)
        tenant_basic_info = driver.find_element(By.LINK_TEXT, "基本信息").text
        print(tenant_basic_info)

        self.assertEqual(page_tenant_name, "湖南健朗药业有限责任公司")
        self.assertEqual(tenant_admin,"管理员")
        self.assertEqual(tenant_basic_info,"基本信息")


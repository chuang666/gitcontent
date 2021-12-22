from selenium import webdriver
from selenium.webdriver.common.by import By
from Constants import *
import time, unittest


class TrialOSPwdLogin(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pwd_login(self):
        #打开浏览器
        global driver
        driver_path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.maximize_window()
        #进入登录页面
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
        driver.find_element(By.XPATH, "//button[@type=\"submit\"]").click()
        time.sleep(2)
        # 验证登录成功
        result = driver.find_element(By.XPATH, "//*[@alt='退出']").get_attribute("alt")
        self.assertEqual(result, "退出")

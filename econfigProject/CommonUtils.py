from selenium import webdriver
import time, pymysql
from selenium.webdriver.common.by import By
from Constants import *


class CommonUtils:

    def __init__(self):
        global driver
        # 打开浏览器
        driver_path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.maximize_window()

    def login_page(self):
        # 进入登录页面
        driver.get(TEST_URL)
        # driver.implicitly_wait(5)
        # 选择密码登录
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@class='toggle-login-text active']").click()
        # 输入用户名、密码
        driver.find_element(By.ID, "username").send_keys(TEST_USER_NAME)
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys(TEST_PWD)
        time.sleep(1)
        # 点击登录
        driver.find_element(By.XPATH, "//button[@type=\"submit\"]").click()
        time.sleep(5)

    def get_quit_element(self):
        result = driver.find_element(By.XPATH, "//*[@alt='退出']").get_attribute("alt")
        return result

    def enter_econfig(self):
        iframe = driver.find_element(By.XPATH, "//div/iframe")
        driver.switch_to.frame(iframe)  # 跳出框架
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//*[@src=\"http://file.test.com/resources/2c948a967b4df83c017b4e36877707df.png\"]").click()
        time.sleep(2)
        # 选择租户并进入
        driver.find_element(By.XPATH, "//div[@title='湖南健朗药业有限责任公司']").click()
        time.sleep(5)

    def get_enter_success_element(self):
        # 取到左上角的租户名字
        a_list = driver.find_element(By.XPATH, "//*[@class='tenant_name']")
        page_tenant_name = a_list.find_element(By.XPATH, "//*[@title='湖南健朗药业有限责任公司']").get_attribute("title")
        # print(page_tenant_name)
        # 取到页面的管理员页签
        tenant_admin = driver.find_element(By.LINK_TEXT, "管理员").text
        # print(tenant_admin)
        # 取到页面的基本信息页签
        tenant_basic_info = driver.find_element(By.LINK_TEXT, "基本信息").text
        # print(tenant_basic_info)
        return page_tenant_name, tenant_admin, tenant_basic_info

    def verify_authorize(self):
        pass

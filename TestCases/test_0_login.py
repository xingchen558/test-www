# -*- coding: utf-8 -*-
# user = www
from selenium import webdriver
import unittest
import ddt
from PageObjects.index_page import IndexPage
from PageObjects.login_page import LoginPage
from TestDatas import common_data as CD
from TestDatas import login_data as TD

@ddt.ddt
class TestLogin(unittest.TestCase):
    @classmethod  # classmethod重点，容易和staticmethod混淆
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(CD.login_url)  # CD.login_url 打开的页面
        cls.driver.maximize_window()
    @classmethod  # classmethod 重点，容易和staticmethod混淆
    def tearDownClass(cls):
        cls.driver.quit()
    def setUp(self):
        pass
    def tearDown(self):
        self.driver.refresh()
    def test_login_2_success(self):
        # 登录 登录功能
        LoginPage(self.driver).login(TD.succ_data["user"], TD.succ_data["pwd"])  # 用户名密码
        # 断言  首页的查询
        self.assertTrue(IndexPage(self.driver).isExist_quitEle())
    @ddt.data(*TD.datas)
    def test_login_0_wrongDatas(self, data):
        # 步骤
        lp = LoginPage(self.driver)
        lp.login(data["user"], data["pwd"])
        # 断言
        self.assertEqual(data["check"], lp.get_errorMsg_from_loginArea())
    @ddt.data(*TD.wrong_data)
    def test_login_1_errorDatas(self, data):
        lp = LoginPage(self.driver)
        lp.login(data['user'], data['pwd'])
        self.assertEqual(data['check'], lp.get_errorMsg_pageCenter())


    # def test_login_noUser(self):
    #     # 步骤
    #     lp = LoginPage(self.driver)
    #     lp.login('', 'python')
    #     # 断言
    #     self.assertEqual("请输入手机号", lp.get_errorMsg_from_loginArea())
    # def test_login_less11(self):
    #     # 步骤
    #     lp = LoginPage(self.driver)
    #     lp.login('1868472', 'python')
    #     # 断言
    #     self.assertEqual("请输入正确手机号", lp.get_errorMsg_from_loginArea())

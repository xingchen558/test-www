# -*- coding: utf-8 -*-
# user = www
# 自动化测试帐号的独立性。
# 1、用例列出 == 前置、步骤、断言
# 2、明确有哪些页面

# 用例1：成功投资场景
"""
前置：1、登陆成功状态；登陆页面 - 首页
      2、可用余额应该大于你要投资的金额；1000
         如何保证在自动化的运行过程中，余额可用。不需要我经常来看用户余额有多少。
         1）充值一笔：33：每次充投资的金额-1000；  ---利用接口直接充值。
         2）暂时充一大笔钱：1个亿。
         3）判断当前用户的余额是否大于投资金额，如果小于，我就大充一笔。如果大于，不用处理。
         要不要查数据库？接口？网页获取？   ---利用接口。
      3、有可投资的标。---在页面就可辨别标是否可投资。---利用元素定位。
         1）新建一个标，并且将标为竞标状态。---接口。
         2）达到1）很复杂。利用现有的环境。
步骤：
    1、首页 - 选标投资。默认选第一个标。
    2.0 标页面 - 金额 输入框中，获取用户的当前余额
    2、标页面 - 金额输入，投资操作。
    3、标页面 - 投资成功的弹出框中，点击 查看并激活
断言：
    1、投资前的余额 - 现在的用户余额  = 投资的钱
    个人页面 - 获取用户可用余额

"""
# 投资失败的场景：
# 1、非100的整数倍
# 2、非10的整数倍
# 3、小数点-非数字-负数-空

# 4、投资的金额(5万)  >  标当前可投的金额(4万)   标+用户的余额同时满足特殊的条件
# 5、投资的金额(5万) >   帐户可用余额(2万)
from selenium.webdriver.common.by import By
import unittest
import time
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.bid_page import BidPage
from PageObjects.user_page import UserPage
from selenium import webdriver
from TestDatas import common_data as CD
from TestDatas import invent_data as TD
from Common.basepage import BasePage
from PageLocators.bidPage_locator import BidPageLocator

class TestInvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 充值 #可投资的标。
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(CD.login_url)
        LoginPage(cls.driver).login(CD.user, CD.pwd)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def setUp(self):
        pass
    def tearDown(self):
        self.driver.refresh()

    def test_invest_3_success(self):
        # 步骤
        # 1、首页 - 选标投资。默认选第一个标。
        # IndexPage(self.driver).click_firstBid()
        # 2.0标页面 - 金额输入框中，获取用户的当前余额
        bp = BidPage(self.driver)
        userMoney_beforeInvest = bp.get_userLeftMoney()
        money_before = int(userMoney_beforeInvest.split('.', 2)[0])
        # 2、标页面 - 金额输入，投资操作。
        bp.invest(TD.money)
        # 3、标页面 - 投资成功的弹出框中，点击查看并激活
        bp.click_activeButton_on_investSuccess_popup()
        # 断言
        userMoney_afterInvest = UserPage(self.driver).get_userLeftMoney()
        money_after = int((userMoney_afterInvest.split("元", 2)[0]).split('.', 2)[0]) + TD.money
        self.assertEqual(money_before, money_after)

    def test_invest_2_failed_no(self):
        bp = BidPage(self.driver)
        bp.invest(0)
        time.sleep(1)
        expected = '请正确填写投标金额'
        BasePage(self.driver).wait_eleVisible(BidPageLocator.invest_failed_popup)
        actual = self.driver.find_element(*BidPageLocator.invest_failed_popup).text
        self.assertEqual(expected, actual)

    def test_invest_1_failed_invalid_data(self):
        # IndexPage(self.driver).click_firstBid()
        bp = BidPage(self.driver)
        bp.invest(-100)
        time.sleep(1)
        expected = '请正确填写投标金额'
        BasePage(self.driver).wait_eleVisible(BidPageLocator.invest_failed_popup)
        actual = self.driver.find_element_by_xpath('//div[@class="text-center"]').text
        self.assertEqual(expected, actual)

    def test_invest_0_failed_no100(self):
        IndexPage(self.driver).click_firstBid()
        bp = BidPage(self.driver)
        bp.invest(150)
        time.sleep(1)
        expected = '投标金额必须为100的倍数'
        # actual = BasePage(self.driver).get_element_attribute(BidPageLocator.invest_failed_popup1, "text-center", "投资_非100倍数")
        BasePage(self.driver).wait_eleVisible(BidPageLocator.invest_failed_popup)
        actual = self.driver.find_element_by_xpath('//div[@class="text-center"]').text
        self.assertEqual(expected, actual)

#
# if __name__ == '__main__':
#     unittest.main()

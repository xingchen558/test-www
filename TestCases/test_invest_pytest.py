# -*- coding: utf-8 -*-
# user = www
import pytest
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
    @pytest.mark.smoke
    @pytest.mark.login
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


# if __name__ == '__main__':
#     unittest.main()

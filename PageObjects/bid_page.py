# -*- coding: utf-8 -*-
# user = www

from PageLocators.bidPage_locator import BidPageLocator as loc
from Common.basepage import BasePage

class BidPage(BasePage):
    # 获取用户余额
    def get_userLeftMoney(self):
        # 等待用户输入框出现
        self.wait_eleVisible(loc.money_input, model_name="标页面_获取用户余额")
        return self.get_element_attribute(loc.money_input, "data-amount", model_name="标页面_获取金额输入框data-amount属性")

    # 投资操作
    def invest(self, money):
        # 等待用户输入框出现
        # 在输入框当中，输入金额
        model = "标页面_投资操作"
        self.wait_eleVisible(loc.money_input, model_name=model)
        self.input_text(loc.money_input, money, model_name=model)
        # 点击投标按钮
        self.click_element(loc.invest_button, model_name=model)

    # 投资成功弹出框、点击查看并激活
    def click_activeButton_on_investSuccess_popup(self):
        name = "标页面_投资成功弹出框_点击查看并激活"
        self.wait_eleVisible(loc.active_button_on_successPop, model_name=name)
        self.click_element(loc.active_button_on_successPop, model_name=name)

    # 错误提示框 - 页面中间
    def get_errorMsg_from_pageCenter(self):
        # 获取文本内容
        # 关闭弹出框
        name = "标页面_页面中间错误提示框"
        self.wait_eleVisible(loc.invest_failed_popup, model_name=name)
        msg = self.get_element_text(loc.invest_failed_popup, model_name=name)
        # 关闭弹出框
        self.click_element(loc.invest_close_failed_popup_button, model_name=name)
        return msg

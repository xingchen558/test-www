# -*- coding: utf-8 -*-
# user = www
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.loginpage_locators import LoginPageLocator as loc
from PageLocators.bidPage_locator import BidPageLocator as boc
from Common.basepage import BasePage
class LoginPage(BasePage):

    def login(self, username, pwd):
        # text 直接得到提示文本
        # * 脱外套
        self.wait_eleVisible(boc.user_phone, model_name="登录页面_登录账号")
        self.input_text(loc.user_input, value=username, model_name='登录账号')
        self.input_text(loc.user_pwd, value=pwd, model_name='登录密码')
        self.click_element(loc.login_button, model_name='登录按钮')
        # WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='phone']")))
        # self.driver.find_element(*loc.user_input).send_keys(username)
        # self.driver.find_element(*loc.user_pwd).send_keys(pwd)
        # self.driver.find_element(*loc.login_button).click()

    def get_errorMsg_from_loginArea(self):
        self.wait_eleVisible(boc.login_error, model_name="登录页面_登录错误")
        return self.get_element_text(loc.errorMsg_from_loginArea, model_name="登录页面_登录错误_1")
        # WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='form-error-info']")))
        # return self.driver.find_element(*loc.errorMsg_from_loginArea).text

    def get_errorMsg_pageCenter(self):
        self.wait_eleVisible(loc.errorMsg_from_pageCenter, model_name="登录页面_登录错误")
        return self.get_element_text(loc.errorMsg_from_pageCenter, model_name="登录页面_登录错误_2")
        # WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='layui-layer-content']")))
        # return self.driver.find_element(*loc.errorMsg_from_pageCenter).text



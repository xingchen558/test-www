# -*- coding: utf-8 -*-
# user = www

from selenium.webdriver.common.by import By

# 元素定位，定位元素，重复使用

class LoginPageLocator:
    # 用户名输入框
    user_input = (By.XPATH, "//input[@name='phone']")
    # 密码输入框
    user_pwd = (By.XPATH, "//input[@name='password']")
    # 登录按钮
    login_button = (By.XPATH, "//button")
    # 错误提示框 - 登录区域
    errorMsg_from_loginArea = (By.XPATH, "//div[@class='form-error-info']")
    # 错误提示框 - 页面中间
    errorMsg_from_pageCenter = (By.XPATH, "//div[@class='layui-layer-content']")

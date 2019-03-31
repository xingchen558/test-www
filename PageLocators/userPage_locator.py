# -*- coding: utf-8 -*-
# user = www


from selenium.webdriver.common.by import By


class UserPageLocator:
    # 可用余额
    user_leftMoney = (By.XPATH, '//li[@class="color_sub"]')

# -*- coding: utf-8 -*-
# user = www
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from PageLocators.userPage_locator import UserPageLocator as uoc
class UserPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    # 获取用户余额
    def get_userLeftMoney(self):
        self.wait_eleVisible(uoc.user_leftMoney, model_name="个人页面_余额")
        return self.get_element_text(uoc.user_leftMoney)
        # WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//li[@class='color_sub']")))
        # return self.driver.find_element(*uoc.user_leftMoney).text



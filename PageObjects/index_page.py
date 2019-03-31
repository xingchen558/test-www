# -*- coding: utf-8 -*-
# user = www
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.indexPage_locator import IndexPageLocator as ioc
from Common.basepage import BasePage
class IndexPage(BasePage):
    #
    # def __init__(self, driver):
    #     self.driver = driver

    def isExist_quitEle(self):
        try:
            self.wait_eleVisible(ioc.quit_button, model_name="首页_退出键")
            # WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='退出']")))
            return True
        except:
            return False

    def click_firstBid(self):
        self.wait_eleVisible(ioc.bid_button, model_name="首页_投资按钮")
        self.click_element(ioc.bid_button, model_name="首页_投资按钮")
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.bid_button))
        # self.driver.find_element(*loc.bid_button).click()







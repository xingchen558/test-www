# -*- coding: utf-8 -*-
# user = www
from Common.log_log import MyLog
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.dir_config import screenshot_dir
import logging
import win32gui
import win32con
import time
import datetime
my_logger = MyLog()
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, timeout=60, poll_frequency=0.5, model_name="model"):
        my_logger.info("等待元素可见：{}".format(locator))
        try:
            # 获取开始等待的时间
            e1 = datetime.datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 获取结束等待的时间
            e2 = datetime.datetime.now()
            # 获取等待的总时长 - 以秒为单位
            e3 = e2 - e1
            my_logger.info("元素已可见。等待元素可见总时长：{},开始等待的时间{},等待结束的时间：{}。".format(e3, e1, e2))
        except:
            # 写进日志
            my_logger.error("等待元素可见超时。")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    # 查找元素
    def get_element(self, locator, model_name="model"):
        my_logger.info("查找模块：{}下的元素：{}".format(model_name, locator))
        try:
            ele = self.driver.find_element(*locator)
            my_logger.info("查元素成功。")
            return ele
        except:
            # 写进日志
            my_logger.error("查找元素失败。")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    # 点击元素
    def click_element(self, locator, model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        my_logger.info("点击操作：模块 {} 下的元素 {}".format(model_name, locator))
        try:
            ele.click()
        except:
            # 写进日志
            my_logger.error("点击元素操作失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    # 输入内容
    def input_text(self, locator, value, model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        my_logger.info("输入操作：模块 {} 下的元素 {}输入文本 {}".format(model_name, locator, value))
        try:
            ele.send_keys(value)
        except:
            # 写进日志
            my_logger.error("元素输入操作失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    # 获取元素的属性
    def get_element_attribute(self, locator, attr, model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        my_logger.info("获取元素属性：模块 {} 下的元素 {} 的属性 {}".format(model_name, locator, attr))
        try:
            return ele.get_attribute(attr)
        except:
            # 写进日志
            my_logger.error("获取元素属性失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    # 获取元素的文本内容
    def get_element_text(self, locator, model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        my_logger.info("获取元素文本值：模块 {} 下的元素 {}".format(model_name, locator))
        try:
            return ele.text
        except:
            # 写进日志
            my_logger.error("获取元素文本值失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    def save_webImg(self, model_name):
        # 文件名称=模块名称_当前时间.png
        filePath = screenshot_dir + "/{0}_{1}.png".format(model_name,
                                                          time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            my_logger.info("截图成功，文件路径为：{}".format(filePath))
        except:
            my_logger.error("截图失败！！")

    # 窗口切换 新的窗口，其他的窗口
    def switch_window(self, str="", index=None):
        if str == "new":
            # 等待新窗口出现
            time.sleep(2)
            windows = self.driver.window_handles
            # 切换到新窗口
            self.driver.switch_to.window(windows[-1])
        else:
            # 获取所有的窗口
            windows = self.driver.window_handles
            if index != None and 0 <= int(index) < len(windows):
                self.driver.switch_to.window(windows[int(index)])
            # 切换到index下标所有的窗口

    # alert切换
    def switch_alert(self, action="accept"):
        # 等待alert出现
        WebDriverWait(self.driver, 15).until(EC.alert_is_present())
        # 关闭alert弹框-accept dismiss
        alert = self.driver.switch_to.alert
        if action == "accept":
            alert.accept()  #  alert类的accept函数
        else:
            alert.dismiss()

    # alert切换
    def switch_iframe(self, iframe_refrence):
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(iframe_refrence))
            time.sleep(0.5)
            self.driver.switch_to.frame(iframe_refrence)
        except:
            # 写进日志
            my_logger.error("切换frame错误")

    # 上传
    def upload(self, filePath, browser_type="chrome"):
        if browser_type == "chrome":
            title = "打开"
        else:
            title = ""
        # 找元素 一级窗口 '#32770', '打开'
        dialog = win32gui.FindWindow('#32770', title)  # 打开--不用浏览器需要改动
        comboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)  # 二级窗口
        comboBox = win32gui.FindWindowEx(comboBoxEx32, 0, 'ComboBox', None)  # 三级窗口
        # 编辑按钮
        Edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级窗口
        # 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, 'Button', '打开(&O)')  # 四级窗口
        # 往编辑当中，输入文件路径
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮


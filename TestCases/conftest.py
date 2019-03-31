# -*- coding: utf-8 -*-
# user = www
import pytest
from selenium import webdriver
from TestDatas import common_data as CD
"""
定义
1、函数名称前面 加上：pytest.fixture #scrope决定作用域，默认是function
2、前值和后置的代码区分：yield
3、如果有返回值，直接写在yield的后面， 用空格 分开

调用：
不支持  unittest
不需要在测试文件当中， 引入 conftest.py
1：测试类或者测试用例中，主动通过 fixture的函数名称  来调用 fixture
  在测试类或者测试用例的前面 ，使用：
2、测试用例 怎么接收。。。  用函数名称
   测试用例如果要使用fixture的返回值，如何接收？
   fixture 的函数名称，就代表他的 返回值
   在测试用例当中，fixture的函数名称作为测试用的参数
"""
driver = None

@pytest.fixture(scope="class")
def prepare_env():
    global driver
    # 前置条件
    print("========测试类级别的fixture======")
    driver = webdriver.Chrome()
    driver.get(CD.login_url)
    driver.maximize_window()
    # 银河
    yield driver
    # 后置条件
    driver.quit()


@pytest.fixture
def refresh_page():
    global driver
    # 前置条件
    print("========测试用例级别的fixture======")
    # 银河
    yield
    # 后置条件
    driver.refresh()


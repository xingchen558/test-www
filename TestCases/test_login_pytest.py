# -*- coding: utf-8 -*-
# user = www
import pytest
import ddt
from PageObjects.index_page import IndexPage
from PageObjects.login_page import LoginPage
from TestDatas import login_data as TD
# self.driver 没有赋值，所以要传入使用 难点。。。
# 测试用例如果要使用fixture的返回值，如何接收？
# fixture 的函数名称，就代表他的 返回值
# 在测试用例当中，fixture的函数名称作为测试用的参数
# @pytest.mark.ff
# def test_failed():
#     assert 100 == 200
# def demo():
#     pass
# @ddt.ddt
@pytest.mark.login
@pytest.mark.usefixtures("prepare_env")
@pytest.mark.usefixtures("refresh_page")
class TestLogin:
    #登陆成功用例
    @pytest.mark.smoke  # 只能运行的smoke的时候才会运行
    def test_login_success(self, prepare_env):
        #步骤：登陆页面的登陆功能 +
        LoginPage(prepare_env).login(TD.succ_data["user"], TD.succ_data["passwd"])
        # 断言：首页的用户查询
        assert IndexPage(prepare_env).isExist_quitEle()

    # def test_login_2_success(self, prepare_env):
    #     # 登录 登录功能
    #     LoginPage(prepare_env).login(TD.succ_data["user"], TD.succ_data["pwd"])  # 用户名密码
    #     # 断言  首页的查询
    #     assert IndexPage(prepare_env).isExist_quitEle()

    # @ddt.data(*TD.datas)
    @pytest.mark.parametrize("data", TD.datas)  # 参数化
    def test_login_wrongDatas(self, data):
        # 步骤
        lp = LoginPage(self.driver)
        lp.login(data["user"], data["pwd"])
        # 断言
        assert data["check"] == lp.get_errorMsg_from_loginArea()

    # @ddt.data(*TD.wrong_data)
    @pytest.mark.parametrize("data", TD.wrong_data)  # 参数化
    def test_login_errorDatas(self, data):
        lp = LoginPage(self.driver)
        lp.login(data['user'], data['pwd'])
        assert data['check'] == lp.get_errorMsg_pageCenter()

pytest.main()

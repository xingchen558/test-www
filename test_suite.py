# -*- coding: utf-8 -*-
# user = www

import HTMLTestRunnerNew
import unittest
from Common import base_path

discover = unittest.defaultTestLoader.discover(base_path.testcase_path,
                                               pattern='test*.py', top_level_dir=None)
with open(base_path.report_path, "wb+") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title='前程贷登录投资测试',
                                              description='测试结果',
                                              tester='星辰')
    runner.run(discover)

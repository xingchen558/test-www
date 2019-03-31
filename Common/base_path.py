# -*- coding: utf-8 -*-
# user = www
import os

base_path = os.path.split(os.path.dirname(__file__))[0]
# print(base_path)
test_path = os.path.join(base_path, 'conf', 'test.conf')
test_cases = os.path.join(base_path, 'cases', 'testcases.xlsx')
log_path = os.path.join(base_path, 'Outputs/Logs', 'log.log')
report_path = os.path.join(base_path, 'Outputs/Reports', 'report.html')
testcase_path = os.path.join(base_path, 'TestCases')
# print(test_path)

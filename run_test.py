#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: run_test.py
# author:liushen
# time:2021/01/04
# 方法三：通过模块来批量加载测试用例
# 创建一个加载器对象
from datetime import datetime
import unittest
from cases import test_01_register


from libs import HTMLTestRunnerNew

from scripts.Do_config import do_config
from scripts.constants import REPORTS_DIR,USER_ACCOUNT_FILE_PATH,CASES_DIR
import os
from scripts.Handle_user import gengerate_users_config
if not os.path.exists(USER_ACCOUNT_FILE_PATH):
	gengerate_users_config()   # 如果用户账号的配置文件不存在 我们就生成配置文件，否则不生成

# 方法四：方法三的补充
# # 1.创建测试加载器，加载所有的测试模块
# one_loader = unittest.TestLoader()
# # 如果有多个测试用例，则要反复添加one_loader.loadTestsFromModule()
# test_moduel_tuple = (one_loader.loadTestsFromModule(test_register),)   # ,one_loader.loadTestsFromModule(module2)  模块2暂时不加
#
# # 2.创建测试套件
# # 创建测试套件时，将所有的测试模块所构成的元组传给TestSuite类
# one_suite = unittest.TestSuite(tests=test_moduel_tuple)   # 这里通过类名+（）来创建对象会调用__init__.py方法，所以这里就不需要addTest

# 如果有多个测试用例，则要反复添加one_loader.loadTestsFromModule()，为了解决这个难点，上面的就都不要了
# 1.创建一个套件，default默认测试加载
one_suite = unittest.defaultTestLoader.discover(CASES_DIR)   # start_dir 模块所在路径，自动搜索cases目录下，test*

# 3.执行用例
# 创建一个运行器对象
# one_runner = unittest.TextTestRunner()   # 因为是对象，所以一定要加(),类+() = 对象，用对象调用
# one_runner.run(one_suite)

# 执行用例 test_results_202012151043.html 需要这种格式
# report_html_name = do_config("file path","report_html_name")

report_html_name = os.path.join(REPORTS_DIR,do_config("report","report_html_name"))
report_html_name_full = report_html_name + "_" + datetime.strftime(datetime.now(),"%Y%m%d%H%M%S") + ".html"

with open(report_html_name_full,mode="wb") as save_to_file:
	one_runner = HTMLTestRunnerNew.HTMLTestRunner(stream=save_to_file,
												  title=do_config("report","title"),
												  verbosity=do_config("report","verbosity"),
												  description=do_config("report","description"),
												  tester=do_config("report","tester"))
	one_runner.run(one_suite)   # 批量执行套件中的测试用例
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: constants.py
# author:liushen
# time:2021/01/01
import os


# 常量最好使用大写
# __file__固定变量  获取当前文件的绝对路径
# 获取项目根目录路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取测试数据datas所在目录的路径
DATAS_DIR = os.path.join(BASE_DIR,"datas")

# 获取配置文件configs所在目录的路径
CONFIGS_DIR = os.path.join(BASE_DIR,"configs")

# 获取日志logs所在目录的路径
LOGS_DIR = os.path.join(BASE_DIR,"logs")

# 获取报告reports所在目录的路径
REPORTS_DIR = os.path.join(BASE_DIR,"reports")

# 获取测试用例cases所在目录的路径
CASES_DIR = os.path.join(BASE_DIR,"cases")

# 获取处理配置文件scripts所在目录的路径
SCRIPTS_DIR = os.path.join(BASE_DIR,"scripts")

#  获取配置文件testcase.conf文件所在目录的路径
CONFIG_FILE_PATH = os.path.join(CONFIGS_DIR,"testcase.conf")

#  获取测试数据test.xlsx文件所在目录的路径
TEST_DATAS_FILE_PATH = os.path.join(DATAS_DIR,"case.xlsx")

# 获取用户人信息数据user_account.conf文件所在目录的路径
USER_ACCOUNT_FILE_PATH = os.path.join(CONFIGS_DIR,"user_account.conf")
pass
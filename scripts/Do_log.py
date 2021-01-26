# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : Do_log.py.py
# author : gaobo
# time : 2020/12/11 0011 18:50
---------------------------------------------------
"""
import logging
from logging.handlers import RotatingFileHandler

from scripts.Do_config import do_config
from scripts.constants import LOGS_DIR
import os
from concurrent_log_handler import ConcurrentRotatingFileHandler

# PermissionError:[WinError 32]另一个程序正在使用此文件，这样的问题就是因为你所有的模块都使用这个日志导致的
# 解决方法一：
# 当前文件不要创建do_log = HandleLog().get_logger()这个对象
# 而是在test开头的测试文件中导入HandleLog这个类，并在测试文件中创建do_log = HandleLog().get_logger()对象来调用
# 解决方法二：
# 通过安装第三方库pip install concurrent-log-handle


class HandleLog:
	"""
	封装处理日志的类
	"""
	def __init__(self):
		self.case_logger = logging.getLogger(do_config("log","logger_name"))
		self.case_logger.setLevel(do_config("log","logger_level"))
		console_handle = logging.StreamHandler()
		# file_handle = RotatingFileHandler(filename=do_config("log","log_filename"),maxBytes=do_config("log","max_byte"),backupCount=do_config("log","backcount"),
		# 									   encoding="utf-8")  # filename选择文件名，那么日志文件就在当前文件夹下，为了解决这个问题，我们要导入日志路径
		# file_handle = RotatingFileHandler(os.path.join(LOGS_DIR,do_config("log","log_filename")),
		# 								  maxBytes=do_config("log","max_byte"),
		# 								  backupCount=do_config("log","backcount"),
		# 								  encoding="utf-8")
		file_handle = ConcurrentRotatingFileHandler(os.path.join(LOGS_DIR,do_config("log","log_filename")),
													maxBytes=do_config("log","max_byte"),
													backupCount=do_config("log","backcount"),
													encoding="utf-8")

		console_handle.setLevel(do_config("log","console_level"))
		file_handle.setLevel(do_config("log","file_level"))
		simple_log = logging.Formatter(do_config("log","simple_log"))
		verbose_log = logging.Formatter(do_config("log","verbose_log"))
		console_handle.setFormatter(simple_log)
		file_handle.setFormatter(verbose_log)
		self.case_logger.addHandler(console_handle)
		self.case_logger.addHandler(file_handle)
		# 这里需要返回一个实例属性，但是构造方法是不能够使用return 所有不能用return self.case_logger，所以我们需要再创建一个实例对象


	def get_logger(self):
		"""
		获取Logger日志器对象
		:return:
		"""
		return self.case_logger
do_log = HandleLog().get_logger()


if __name__ == '__main__':
	case_logger = HandleLog().get_logger()
	case_logger.debug("这是debug收集器")
	case_logger.info("这是info收集器")
	case_logger.warning("这是warning收集器")
	case_logger.error("这是error收集器")
	case_logger.critical("这是critical收集器")



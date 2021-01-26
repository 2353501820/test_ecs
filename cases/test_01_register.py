#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: test_01_register.py
# author:liushen
# time:2021/01/03
import unittest
from libs.ddt import ddt,data
import inspect
from scripts.Handle_request import HttpRequest
from scripts.Do_excel import HandleExcel
from scripts.Do_config import do_config
from scripts.Do_log import do_log
from scripts import constants
from scripts.Handle_context import Context

# do_excel = HandleExcel(do_config("file path","test_path"),"multi")
do_excel = HandleExcel(constants.TEST_DATAS_FILE_PATH,"register")

@ddt
class TestRegister(unittest.TestCase):  # unittest规则：每一条用例，使用实例方法来测试，并且实例方法吗要以test_开头
	"""
	测试注册功能
	"""

	tests = do_excel.get_tests()

	@classmethod
	def setUpClass(cls):
		"""
		重写父类类方法，在实例方法执行之前会被调用一次
		:return:
		"""
		cls.send_request = HttpRequest()
		do_log.info("\n{:=^40s}".format("开始执行注册功能用例"))


	@classmethod
	def tearDownClass(cls):
		"""
		重写父类类方法，在实例方法执行结束之后会被调用一次
		:return:
		"""
		cls.send_request.close()
		do_log.info("\n{:=^40s}".format("注册功能用例执行结束"))


	@data(*tests)
	def test_register(self,data_namedtuple):
		"""
		测试注册功能
		:return:
		"""
		# print("\nrunning test method:{}".format(inspect.stack()[0][3]))
		do_log.info("\nrunning test method:{}".format(inspect.stack()[0][3]))
		# 		获取两个负数相乘的结果

		# 将实际结果写入Excel
		run_success_msg = do_config("msg", "success_result")

		run_fail_msg = do_config("msg", "fail_result")

		new_data = Context.register_parameterization(data_namedtuple.data)

		new_url = do_config("api","prefix_url") + data_namedtuple.url

		response = self.send_request(data_namedtuple.method,url=new_url,data=new_data)


		try:
			self.assertEqual(data_namedtuple.expected, response.text, msg="测试{}失败".format(data_namedtuple.title))
		except AssertionError as e:
			do_log.error("具体异常为：{}".format(e))
			do_excel.write_result(row=data_namedtuple.case_id + 1, actual=response.text, result=do_config("msg", "fail_result"))
			# self.assertRaises(TypeError)   # assertRaises可以直接断言异常
			# raise关键字是将某个异常主动抛出
			raise e
		else:
			# ws.cell(row=case_id+1,column=7,value="Pass")
			# self.test_obj.write_result(row=case_id+1,actual=real_result,result="Pass")
			do_excel.write_result(row=data_namedtuple.case_id+1,actual=response.text,result=do_config("msg","success_result"))
		# self.file.write("{}，执行结果为：{}\n".format(msg,run_success_msg))

if __name__ == '__main__':
	unittest.main()
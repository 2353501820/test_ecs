#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: test_05_invest.py
# author:liushen
# time:2021/01/07
import unittest
from libs.ddt import ddt,data
import inspect
import json
from scripts.Handle_request import HttpRequest
from scripts.Do_excel import HandleExcel
from scripts.Do_config import do_config
from scripts.Do_log import do_log
from scripts import constants
from scripts.Handle_context import Context
from scripts.Handle_mysql_encapsulation import HandleMysql

# do_excel = HandleExcel(do_config("file path","test_path"),"multi")
do_excel = HandleExcel(constants.TEST_DATAS_FILE_PATH,"invest")
# LOAN_ID = None 因为只要第一次导入的时候有效，LOAN_ID是改变的话 Context是不会变的，所以我们不能把它设为全局变量

@ddt
class TestInvest(unittest.TestCase):  # unittest规则：每一条用例，使用实例方法来测试，并且实例方法吗要以test_开头
	"""
	测试投资功能
	"""

	tests = do_excel.get_tests()

	@classmethod
	def setUpClass(cls):
		"""
		重写父类类方法，在实例方法执行之前会被调用一次
		:return:
		"""
		cls.send_request = HttpRequest()
		cls.handle_mysql = HandleMysql()
		do_log.info("\n{:=^40s}".format("开始执行投资功能用例"))


	@classmethod
	def tearDownClass(cls):
		"""
		重写父类类方法，在实例方法执行结束之后会被调用一次
		:return:
		"""
		cls.send_request.close()
		cls.handle_mysql.close()
		do_log.info("\n{:=^40s}".format("投资功能用例执行结束"))


	@data(*tests)
	def test_invest(self,data_namedtuple):
		"""
		测试投资功能
		:return:
		"""
		do_log.info("\nrunning test method:{}".format(inspect.stack()[0][3]))

		# 将实际结果写入Excel
		run_success_msg = do_config("msg", "success_result")

		run_fail_msg = do_config("msg", "fail_result")

		new_data = Context.invest_parameterization(data_namedtuple.data)

		new_url = do_config("api","prefix_url") + data_namedtuple.url

		response = self.send_request(data_namedtuple.method,url=new_url,data=new_data)
		# 如果code因为网络不好或者其他原因获取不到，那么我们就不需要往下执行了，所以这边也加个断言
		try:
			self.assertEqual(200,response.status_code,msg="测试{}请求失败，状态码为{}".format(data_namedtuple.title,response.status_code))
		except AssertionError as e:
			do_log.error("具体异常为{}".format(e))
			raise

		# 如果接口返回的是加标成功，再判断sql
		if response.json().get("msg") == "加标成功":
			check_sql = data_namedtuple.check_sql
			if check_sql:
				check_sql = Context.invest_parameterization(check_sql)
				mysql_data = self.handle_mysql(check_sql)
				# 获取标ID
				# loan_id = mysql_data.get("Id")
				# 标ID要获取全局的
				# global LOAN_ID
				# LOAN_ID = mysql_data.get("Id")
				# 给Context创建一个loan_id的类属性
				# 方法一：
				Context.loan_id = mysql_data.get("Id")
				# 方法二：（方法一更好理解）
				# setattr(Context,"loan_id")


		code = response().json().get["code"]
		try:
			# excel当中的expected是数字类型，但是.json.get[]获取的是字符串，所以我们断言时得转换成字符串类型
			self.assertEqual(str(data_namedtuple.expected), code, msg="测试{}失败".format(data_namedtuple.title))
			# 我们上面断言了状态码，但是充值金额没有断言，所以还要继续断言下充值金额



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
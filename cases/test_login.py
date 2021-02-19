#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: test_login.py
# author:gaobo
# time:2021/02/17
import os
import unittest
from libs.ddt import ddt, data
import inspect
import json
from scripts.Handle_request import HttpRequest
from scripts.Do_excel import HandleExcel
from scripts.Do_config import do_config
from scripts.Do_log import do_log
from scripts import constants
from scripts.Handle_context import Context
from scripts.Handle_mysql_encapsulation import HandleMysql

case_path = os.path.join(constants.DATAS_DIR, 'login.xlsx')

do_excel = HandleExcel(case_path)


@ddt
class TestLogin(unittest.TestCase):
	"""
	测试登录接口
	"""
	all_case = do_excel.get_tests()

	@classmethod
	def setUpClass(cls):
		"""
		执行用例前调用
		:return:
		"""
		cls.send_request = HttpRequest()
		do_log.info("\n{:=^40s}".format("开始执行登录接口用例"))

	@classmethod
	def tearDownClass(cls):
		"""
		所有用例结束后调用
		:return:
		"""
		cls.send_request.close_session()
		do_log.info("\n{:=^40s}".format("登录接口用例执行结束"))

	@data(*all_case)
	def test_login(self, data_namedtuple):
		do_log.info("\nrunning test method:{}".format(inspect.stack()[0][3]))
		data = data_namedtuple.data
		url = do_config("login", "url") + data_namedtuple.url
		res = self.send_request(method=data_namedtuple.method, url=url,data=data)
		# result = res.json()
		if data_namedtuple.id == 1:
			self.assertEqual(res.json()['login'],data_namedtuple.expected,msg='{}的期望值与实际值不一致'.format(data_namedtuple.title))
		elif data_namedtuple.id == 2:
			self.assertEqual(res.json()['login'],data_namedtuple.expected,msg='{}的期望值与实际值不一致'.format(data_namedtuple.title))
		elif data_namedtuple.id == 3:
			self.assertEqual(res.json()['login'],data_namedtuple.expected,msg='{}的期望值与实际值不一致'.format(data_namedtuple.title))
		elif data_namedtuple.id == 4:
			self.assertEqual(res.status_code,data_namedtuple.expected,msg='{}的期望值与实际值不一致'.format(data_namedtuple.title))
		elif data_namedtuple.id == 5:
			self.assertEqual(res.status_code,data_namedtuple.expected,msg='{}的期望值与实际值不一致'.format(data_namedtuple.title))
		elif data_namedtuple.id == 6:
			self.assertEqual(res.json()['rows'][0]['status'],data_namedtuple.expected,msg='{}的期望值与实际值不一致'.format(data_namedtuple.title))
		elif data_namedtuple.id == 7:
			self.assertEqual(res.json()['rows'][0]['status'],data_namedtuple.expected,msg='{}的期望值与实际值不一致'.format(data_namedtuple.title))
		else:
			self.assertEqual(res.json()['rows'][0]['status'],data_namedtuple.expected,msg='{}的期望值与实际值不一致'.format(data_namedtuple.title))


if __name__ == '__main__':
	unittest.main()

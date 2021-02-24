#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: test_06_add_patient.py
# author:gaobo
# time:2021/02/19
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


add_patient_path = os.path.join(constants.DATAS_DIR,"add_patient.xlsx")
do_excel = HandleExcel(add_patient_path)

@ddt
class TestAddPatient(unittest.TestCase):
	"""
	测试新增患者测试用例
	"""
	all_tests = do_excel.get_tests()

	@classmethod
	def setUpClass(cls):
		cls.sent_request = HttpRequest()
		do_log.info("\n{:=^40s}".format("开始执行新增患者功能用例"))

	@classmethod
	def tearDownClass(cls):
		cls.sent_request.close_session()
		do_log.info("\n{:=^40s}".format("新增患者功能用例执行结束"))

	@data(*all_tests)
	def test_add_patient(self,data_namedtuple):
		do_log.info("\nrunning test method:{}".format(inspect.stack()[0][3]))
		data = Context().add_patient_parameterization(data_namedtuple.data)
		id = data_namedtuple.id
		method = data_namedtuple.method
		title = data_namedtuple.title
		url = do_config("login", "url") + data_namedtuple.url
		result = self.sent_request(method=method, url=url, data=data)
		if id == 1:
			self.assertEqual(result.status_code, data_namedtuple.expected, msg="{}期望值与实际值不一致".format(title))
		elif id == 2:
			self.assertEqual(result.status_code, data_namedtuple.expected, msg="{}期望值与实际值不一致".format(title))
		else:
			self.assertEqual(result.json()["message"], data_namedtuple.expected, msg="{}期望值与实际值不一致".format(title))


if __name__ == '__main__':
	unittest.main()

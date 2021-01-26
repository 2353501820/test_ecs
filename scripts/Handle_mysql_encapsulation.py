#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: Handle_mysql_encapsulation.py
# author:liushen
# time:2020/12/31
import pymysql
import random
from scripts.Do_config import do_config

class HandleMysql:
	"""
	处理mysql
	"""
	def __init__(self):
		self.conn = pymysql.connect(host=do_config("mysql","host"),
							   user=do_config("mysql","user"),
							   password=do_config("mysql","password"),
							   db=do_config("mysql","db"),
							   port=do_config("mysql","port"),
							   charset=do_config("mysql","charset"),
							   cursorclass=pymysql.cursors.DictCursor)
		self.cursor = self.conn.cursor()

	# def get_value(self,sql,args=None):
	# 	"""
	# 	获取单个值
	# 	:param sql:
	# 	:param arg:
	# 	:return:
	# 	"""
	# 	self.cursor.execute(sql,args)
	# 	self.conn.commit()
	#
	# 	return self.cursor.fetchone()
	#
	# def get_values(self,sql,args=None):
	# 	"""
	# 	获取多个值
	# 	:param sql:
	# 	:param args:
	# 	:return:
	# 	"""
	# 	self.cursor.execute(sql,args)
	# 	self.conn.commit()
	#
	# 	return self.cursor.fetchall()
	# 两个一模一样的方法可以封装在一块 显得更高级 用__call__

	def __call__(self,sql,args=None,is_more=False):
		"""

		:param sql:sql语句，字符类型
		:param args:sql语句的参数，序列类型
		:param is_more:bool类型
		:return:字典或者嵌套字典的列表
		"""
		self.cursor.execute(sql,args)
		self.conn.commit()
		if is_more == True:
			result = self.cursor.fetchall()
		else:
			result = self.cursor.fetchone()
		return result

	@staticmethod
	def creat_mobile():
		"""
		随机创建手机号
		:return:
		"""
		start_mobile = ["134","135","136","137","138","139","150","151","152","157","158","159","182","183","184","187","188","189",
						"178","130","131","132","155","156","185","186","176","133","153","180","181","177"]
		start_num = random.choice(start_mobile)   # 参数为序列类型choice必须为序列类型
		one_str = "0123456789"
		end_num = "".join(random.sample(one_str))
		return start_num + end_num

	def is_existed_mobile(self,mobile):
		"""
		判断给定的手机号在数据库中是否存在
		:param mobile: 待判断的手机号，为字符串类型
		:return:
		"""
		sql = "SELECT `MobilePhone` FROM future.`member` WHERE `MobilePhone`=%s;"
		if self(sql=sql,args=(mobile,)):
			return True
		else:
			return False

	def creat_not_existed_mobile(self):
		"""
		创建一个不存在的手机号
		:return:
		"""
		while True:
			one_mobile = self.creat_mobile()
			if not self.is_existed_mobile(one_mobile):
				break
		return one_mobile


	def mysql_close(self):
		"""
		关闭mysql
		:return:
		"""
		self.cursor.close()
		self.conn.close()


if __name__ == '__main__':
	sql_1 = "SELECT * FROM `member` LIMIT 0,10;"
	sql_2 = "SELECT * FROM `member` WHERE LeaveAmount > %s LIMIT 0,10;"
	#
	do_mysql = HandleMysql()
	print(do_mysql(sql=sql_1,is_more=False))
	do_mysql(sql=sql_2,args=(400,),is_more=True)

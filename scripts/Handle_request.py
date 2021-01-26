#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: Handle_request.py
# author:gaobo
# time:2020/12/29
import requests
import json
from scripts.Do_log import do_log
class HttpRequest:
	"""
	处理请求
	"""
	def __init__(self):
		# 创建一个Session对象，赋值为HttpRequest对象的属性one_session
		self.one_session = requests.Session()

	def __call__(self,method,url,data=None,is_json=False,**kwargs):
		method = method.lower()
		if isinstance(data,str):
			try:
				data = json.loads(data)
			except Exception as e:
				# print(e)
				do_log.error("将json转换为Python数据类型时出现异常，异常为{}".format(e))
				data=eval(data)
		if method == "get":
			res = self.one_session.request(method=method,url=url,params=data,**kwargs)
		elif method == "post":
			if is_json:
				res = self.one_session.request(method=method,url=url,json=data,**kwargs)   # 如果使用json格式来传参
			else:
				res = self.one_session.request(method=method,url=url,data=data,**kwargs)
		else:
			res = None
			do_log.error("不支持【{}】请求方法".format(method))
		return res

	def close_session(self):
		self.one_session.close()


if __name__ == '__main__':
	login_url = "http://test.lemonban.com:8080/futureloan/mvc/api/member/login"
	recharge_url = "http://test.lemonban.com:8080/futureloan/mvc/api/member/recharge"
	login_params = {"mobilephone":"13900001111",
					"pwd":"123456"}
	recharge_params = {"mobilephone":"13900001111",
				   "amount":"500"}
	headers = {"Content_Type":"application/doc"}
	send_request = HttpRequest()
	# 登录
	res_1=send_request(method="post",url=login_url,data=login_params,is_json=True,headers=headers)
	# 充值
	res = send_request(method="pOST",url=recharge_url,data=recharge_params)
pass
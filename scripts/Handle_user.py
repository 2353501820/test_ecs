#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: Handle_user.py
# author:liushen
# time:2021/01/04
from scripts.Handle_mysql_encapsulation import HandleMysql
from scripts.Handle_request import HttpRequest
from scripts.Do_config import do_config
from scripts.constants import CONFIGS_DIR


def creat_new_user(regname,password:"123456"):
	"""
	创建一个用户
	:param regame:用户名
	:param password:密码
	:return:
	"""
	handle_mysql = HandleMysql()
	send_request = HttpRequest()
	url = do_config("api","prefix_url") + "/member/register"
	sql = "SELECT `Id` FROM future.`member` WHERE `MobilePhone`=%s;"
	while True:
		mobile = handle_mysql.creat_not_existed_mobile()
		data = {"mobilephone":mobile,"pwd":password,"regame":regname}
		send_request(method="post",url=url,data=data)
		result = handle_mysql(sql=sql,args=(mobile,))
		if result:
			user_id = result['Id']
			break

	user_dict = {
		regname:{"Id":user_id,"mobile":mobile,"password":password,"regname":regname}
	}

	handle_mysql.mysql_close()
	send_request.close_session()
	return user_dict

def gengerate_users_config():
	"""
	生成三个用户信息
	:return:
	"""
	user_datas_dict = {}
	user_datas_dict.update(creat_new_user("admin_user"))
	user_datas_dict.update(creat_new_user("invest_user"))
	user_datas_dict.update(creat_new_user("borrow_user"))
	do_config.write_config(user_datas_dict,CONFIGS_DIR)
	# return user_datas_dict

if __name__ == '__main__':
	# do_config.write_config(gengerate_users_config(),"user_accounts.conf")
	gengerate_users_config()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: GetValue.py
# author:gaobo
# time:2020/05/18

import jsonpath
import json
class GetValue:
	'''
	取接口返回值
	'''
	def __init__(self,data):
		'''
		data: 返回值数据
		'''
		try:
			self.data =json.loads(data)   #json转成字典
		except Exception :
			self.data = data
	def __call__(self,key,num=0,is_all=False):
		'''
		key：要取的value的key值
		num：返回值里如果有多个相同的key，返回列表，就再传个列表的下标，默认是0，可以不传
		'''
		if is_all == True:
			data = jsonpath.jsonpath(self.data,'$..{}'.format(key))
		else:
			data = jsonpath.jsonpath(self.data,'$..{}'.format(key))
			data =data[num]
		return data



if __name__ == '__main__':
	a ={'data': {'pageNum': 1, 'pageSize': 10, 'total': 116, 'pages': 12, 'list': [{'id': 315908, 'instNo': '7a0f8eab388e456ba62c4995a23ba990', 'defNo': 'znlhzl_ser_task_meet_danger', 'taskNo': 'deal_ser_task_meet_danger', 'sortOrder': 30, 'prevTaskNo': 'create_ser_task_meet_danger', 'nextTaskNo': 'finish_ser_task_meet_danger', 'createBy': 'USER2004035252', 'createTime': '2020-05-18 16:42:24', 'comment': '', 'status': 1, 'deleteFlag': 0, 'upateTime': '2020-05-18 16:42:25', 'tenantNo': '', 'bizNo': 'RW2020100604', 'procDefName': '服务工单-出险', 'updateBy': 'USER1904031905', 'creatorName': '付世俊', 'updatorName': '姚晓辉', 'stepName': '处理', 'defType': 1, 'bizType': 113, 'title': '付世俊的服务工单-出险'}, {'id': 315634, 'instNo': '7fbad3b0f37d46b5b74cefa24834474f', 'defNo': 'znlhzl_ser_task_meet_danger', 'taskNo': 'deal_ser_task_meet_danger', 'sortOrder': 30, 'prevTaskNo': 'create_ser_task_meet_danger', 'nextTaskNo': 'finish_ser_task_meet_danger', 'createBy': 'USER2004035252', 'createTime': '2020-05-18 15:31:56', 'comment': '', 'status': 1, 'deleteFlag': 0, 'upateTime': '2020-05-18 15:31:58', 'tenantNo': '', 'bizNo': 'RW2020100573', 'procDefName': '服务工单-出险', 'updateBy': 'USER1904031905', 'creatorName': '付世俊', 'updatorName': '姚晓辉', 'stepName': '处理', 'defType': 1, 'bizType': 113, 'title': '付世俊的服务工单-出险'}, {'id': 315228, 'instNo': 'c0e1b764952f408693ac733fb8037c19', 'defNo': 'znlhzl_ser_task_jsc', 'taskNo': 'deal_ser_task_jsc', 'sortOrder': 30, 'prevTaskNo': 'create_ser_task_jsc', 'nextTaskNo': 'finish_ser_task_jsc', 'createBy': 'USER2005035514', 'createTime': '2020-05-15 09:11:58', 'comment': '', 'status': 1, 'deleteFlag': 0, 'upateTime': '2020-05-15 09:11:59', 'tenantNo': '', 'bizNo': 'RW2020100539', 'procDefName': '服务工单-手动解锁车', 'updateBy': 'USER1904031905', 'creatorName': '薛飞HU', 'updatorName': '姚晓辉', 'stepName': '处理', 'defType': 1, 'bizType': 116, 'title': '薛飞HU的服务工单-手动解锁车'}, {'id': 315227, 'instNo': '2e4f87fbb17b4367b9892f6a61461d2f', 'defNo': 'znlhzl_ser_task_jsc', 'taskNo': 'deal_ser_task_jsc', 'sortOrder': 30, 'prevTaskNo': 'create_ser_task_jsc', 'nextTaskNo': 'finish_ser_task_jsc', 'createBy': 'USER2005035514', 'createTime': '2020-05-15 09:09:01', 'comment': '', 'status': 1, 'deleteFlag': 0, 'upateTime': '2020-05-15 09:09:02', 'tenantNo': '', 'bizNo': 'RW2020100538', 'procDefName': '服务工单-手动解锁车', 'updateBy': 'USER1904031905', 'creatorName': '薛飞HU', 'updatorName': '姚晓辉', 'stepName': '处理', 'defType': 1, 'bizType': 116, 'title': '薛飞HU的服务工单-手动解锁车'}, {'id': 315226, 'instNo': '6159d8597c42420688c56f0f8f1e8962', 'defNo': 'znlhzl_ser_task_jsc', 'taskNo': 'deal_ser_task_jsc', 'sortOrder': 30, 'prevTaskNo': 'create_ser_task_jsc', 'nextTaskNo': 'finish_ser_task_jsc', 'createBy': 'USER2005035514', 'createTime': '2020-05-15 09:08:30', 'comment': '', 'status': 1, 'deleteFlag': 0, 'upateTime': '2020-05-15 09:08:31', 'tenantNo': '', 'bizNo': 'RW2020100537', 'procDefName': '服务工单-手动解锁车', 'updateBy': 'USER1904031905', 'creatorName': '薛飞HU', 'updatorName': '姚晓辉', 'stepName': '处理', 'defType': 1, 'bizType': 116, 'title': '薛飞HU的服务工单-手动解锁车'}, {'id': 315225, 'instNo': '2ae72871368949e5ad53c9715441878a', 'defNo': 'znlhzl_ser_task_jsc', 'taskNo': 'deal_ser_task_jsc', 'sortOrder': 30, 'prevTaskNo': 'create_ser_task_jsc', 'nextTaskNo': 'finish_ser_task_jsc', 'createBy': 'USER2005035514', 'createTime': '2020-05-15 09:06:05', 'comment': '', 'status': 1, 'deleteFlag': 0, 'upateTime': '2020-05-15 09:06:06', 'tenantNo': '', 'bizNo': 'RW2020100536', 'procDefName': '服务工单-手动解锁车', 'updateBy': 'USER1904031905', 'creatorName': '薛飞HU', 'updatorName': '姚晓辉', 'stepName': '处理', 'defType': 1, 'bizType': 116, 'title': '薛飞HU的服务工单-手动解锁车'}, {'id': 315224, 'instNo': '6e69c34df23142e7b9cc8a2339dc72ff', 'defNo': 'znlhzl_ser_task_jsc', 'taskNo': 'deal_ser_task_jsc', 'sortOrder': 30, 'prevTaskNo': 'create_ser_task_jsc', 'nextTaskNo': 'finish_ser_task_jsc', 'createBy': 'USER2005035514', 'createTime': '2020-05-14 19:53:42', 'comment': '', 'status': 1, 'deleteFlag': 0, 'upateTime': '2020-05-14 19:53:43', 'tenantNo': '', 'bizNo': 'RW2020100535', 'procDefName': '服务工单-手动解锁车', 'updateBy': 'USER1904031905', 'creatorName': '薛飞HU', 'updatorName': '姚晓辉', 'stepName': '处理', 'defType': 1, 'bizType': 116, 'title': '薛飞HU的服务工单-手动解锁车'}, {'id': 315223, 'instNo': 'a66bad8331334f5ba7e0398ac214e5af', 'defNo': 'znlhzl_ser_task_jsc', 'taskNo': 'deal_ser_task_jsc', 'sortOrder': 30, 'prevTaskNo': 'create_ser_task_jsc', 'nextTaskNo': 'finish_ser_task_jsc', 'createBy': 'USER2005035514', 'createTime': '2020-05-14 19:51:00', 'comment': '', 'status': 1, 'deleteFlag': 0, 'upateTime': '2020-05-14 19:51:00', 'tenantNo': '', 'bizNo': 'RW2020100534', 'procDefName': '服务工单-手动解锁车', 'updateBy': 'USER1904031905', 'creatorName': '薛飞HU', 'updatorName': '姚晓辉', 'stepName': '处理', 'defType': 1, 'bizType': 116, 'title': '薛飞HU的服务工单-手动解锁车'}, {'id': 315222, 'instNo': 'e10eca62986b49d4b953b75ac1e4f4a7', 'defNo': 'znlhzl_ser_task_jsc', 'taskNo': 'deal_ser_task_jsc', 'sortOrder': 30, 'prevTaskNo': 'create_ser_task_jsc', 'nextTaskNo': 'finish_ser_task_jsc', 'createBy': 'USER2005035514', 'createTime': '2020-05-14 19:48:39', 'comment': '', 'status': 1, 'deleteFlag': 0, 'upateTime': '2020-05-14 19:48:39', 'tenantNo': '', 'bizNo': 'RW2020100533', 'procDefName': '服务工单-手动解锁车', 'updateBy': 'USER1904031905', 'creatorName': '薛飞HU', 'updatorName': '姚晓辉', 'stepName': '处理', 'defType': 1, 'bizType': 116, 'title': '薛飞HU的服务工单-手动解锁车'}, {'id': 315221, 'instNo': '358ec3143f044fb68dde501eb050e76e', 'defNo': 'znlhzl_ser_task_jsc', 'taskNo': 'deal_ser_task_jsc', 'sortOrder': 30, 'prevTaskNo': 'create_ser_task_jsc', 'nextTaskNo': 'finish_ser_task_jsc', 'createBy': 'USER2005035514', 'createTime': '2020-05-14 19:43:06', 'comment': '', 'status': 1, 'deleteFlag': 0, 'upateTime': '2020-05-14 19:43:06', 'tenantNo': '', 'bizNo': 'RW2020100532', 'procDefName': '服务工单-手动解锁车', 'updateBy': 'USER1904031905', 'creatorName': '薛飞HU', 'updatorName': '姚晓辉', 'stepName': '处理', 'defType': 1, 'bizType': 116, 'title': '薛飞HU的服务工单-手动解锁车'}], 'isFirstPage': True, 'isLastPage': False}, 'message': 'ok', 'success': True, 'errCode': 0}

	c = a['data']['list'][1]['id']    #原本取多层嵌套里的第2个列表id字段需要拼很长
	#示例
	b = GetValue(a)('id',num=1)    #使用方法取值，有多个key值的，就再传个列表的下标，默认是0，可以不传,如果需要去全部的就传is_all=True
	#使用方式，类名(数据)(key名)
	print(b)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: VariousTime.py
# author:gaobo
# time:2020/07/10


import time
import arrow
import calendar, datetime

now = datetime.datetime.now()  # 当前时间 格式：2020-07-10 09:17:39.350268
now_arr = arrow.now()     # 当前时间 格式：2020-07-11T08:50:57.634640+08:00


class VariousTime:
	'''
	返回各种格式的时间和日期
	'''

	@staticmethod
	def get_specified_time(years =0,months =0,weeks =0,days =0 ,hours =0, is_date =False):

		'''
		 获取指定年月日小时的指定时间
		可以左右两边进行加减移位操作，加减的对象可以是年月日时分秒和星期
		想指定哪个就传哪个，也可以是组合加减，
		@param years: 年 int数字   不传默认0当前年份
		@param months: 月 int数字   不传默认0当前月份
		@param weeks: 周 int数字   不传默认0,例：今天周五，如为-1则返回上周五日期
		@param days: 日 int数字   不传默认0当日
		@param hours: 小时 int数字   不传默认0当前小时
		@param is_date: 默认是False  为True 则返回日期
		@return: 返回时间
		'''
		today_date = now_arr.shift(years=years,months=months,weeks=weeks,days=days,hours=hours)
		today_date = today_date.format("YYYY-MM-DD") if is_date==True else today_date.format("YYYY-MM-DD HH:mm:ss")
		return today_date

	@staticmethod
	def beginning_and_end_of_month():
		'''
		返回每月第一天和最后一天，格式 2020-07-01和2020-07-31
		@return: start 每月第一天 ，end 每月最后一天
		'''
		year = now.year
		month = now.month
		last_day = calendar.monthrange(year, month)[1]  ## 最后一天
		start = datetime.date(year, month, 1)  # 每月第一天
		end = datetime.date(year, month, last_day)  # 每月最后一天
		return start, end

	@staticmethod
	def timestamp_conversion_time(timestamp_num, is_date=False):
		'''
		10位或者13位的时间戳，转出正常格式的时间
		 is_date为True 返回日期格式：2020-07-09，False 返回时间格式：2020-07-09 09:30:13
		@param timenum: 时间戳
		@param is_date:  默认是False  为True 则返回日期
		@return: 返回时间
		'''
		time_num = int(timestamp_num) if type(timestamp_num) != 'int' else timestamp_num  # 不是int型转成int
		timestamp = time_num if len(str(time_num)) == 10 else float(time_num / 1000)  # 10位数直接返回，不是10位数默认就是13位
		time_array = time.localtime(timestamp)
		other_style_time = time.strftime("%Y-%m-%d", time_array) if is_date == True else time.strftime(
			"%Y-%m-%d %H:%M:%S", time_array)  # is_date为真返回日期，不然返回时间
		return other_style_time





if __name__ == '__main__':
	a = VariousTime.get_specified_time(weeks=-2,is_date=True)
	print(a)

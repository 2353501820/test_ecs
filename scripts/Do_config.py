# -*- coding: utf-8 -*-
"""
--------------------------------------------------
# file : Do_config.py
# author : liushen
# time : 2020/11/30 0030 22:24
---------------------------------------------------
"""
# 1.明确需求
# 通过区域名和选项名来获取选项值
# 如果只传区域名，能获取此区域下的所有选项，返回一个字典
# 如果获取到的数据为数字类型的字符串，自动转化为python中的数字类型

# 2.把固定的参数设置为属性

# 3.综合需求
# 一个对象(区域名，选项名)   # 通过区域名和选项名来获取选项值
# 一个对象(区域名)   # 能获取此区域下的所有选项，返回一个字典
# 一个对象()   # 返回DEFAULT默认区域下的所有选项，构造成的一个字典
# 一个对象(is_eval=True)   # 将获取到的数据使用eval函数进行转换
# 一个对象(is_bool=True)   # 将获取到的数据使用getboolean()方法来获取


# class Foo:
# 	def __str__(self):
# 		return "我家静宝"
#
# 	def __call__(self, a,b):
# 		pass
#
# obj = Foo()
# obj(10,20)   # 一个对象使用括号（类似于函数的调用），那么会自动调用__call__()这个实例方法

# 一个类名+括号 Foo()会调用__init__()方法
# 一个对象+括号 obj()会调用__call__()方法
# print打印一个对象，会自动调用__str__()方法

from configparser import ConfigParser
from scripts.constants import CONFIG_FILE_PATH,CONFIGS_DIR
import os


class Handleconfig(ConfigParser):
	"""
	定义处理配置文件的类
	"""
	def __init__(self,filename=None):   # 对父类的构造方法进行拓展
		# 调用父类的构造方法
		super().__init__()
		# self.filename = CONFIG_FILE_PATH
		self.filename = filename
		# self.read(self.filename,encoding="utf-8")   # 读取配置文件


	def __call__(self, section="DEFAULT",option=None,is_eval=False,is_bool=False):
		"""
		'对象()'这种形式，__call__方法会被调用
		:param section:区域名
		:param option:选项名
		:param is_eval:为默认参数，是否进行eval函数转换，默认不转换
		:param is_bool:选项对应的值是否需要转换为bool类型，默认不转换
		:return:
		"""
		self.read(self.filename,encoding="utf-8")   # 读取配置文件
		if option is None:
			# 一个对象(区域名)   # 能获取此区域下的所有选项，返回一个字典
			return dict(self[section])

		if isinstance(is_bool,bool):
			if is_bool:
				return self.getboolean(section,option)
		else:
			raise ValueError("is_bool 必须是布尔类型")  # 手动抛出异常

		data = self.get(section,option)
		# 如果获取到的数据为数字类型的字符串，自动转化为python中的数字类型
		if data.isdigit():   # 判断是否为数字类型的字符串
			return int(data)
		try:
			return float(data)   # 如果是浮点型的字符串则直接转换
		except ValueError:
			pass

		# 一个对象(is_eval=True)   # 将获取到的数据使用eval函数进行转换
		if isinstance(is_eval,bool):
			if is_eval:
				return eval(data)
		else:
			raise ValueError("is_eval")
		return data

	@classmethod
	def write_config(cls,data,filename):
		"""
		将数据写入到配置文件
		:param data:字典类型的数据
		:param filename:配置文件名，字符串
		:return:
		"""
		config = cls(filename=filename)   # cls是类本身，类本身+()相当于新创建了一个对象，就不会覆盖原来的配置文件了
		for key in data:
			config[key] = data[key]   # 因为上面已经打开了一个配置文件，如果这边还是用self相当于覆盖了。而我们的诉求是创建一个新的配置文件

		filename = os.path.join(CONFIGS_DIR,filename)
		with open(filename,mode="w",encoding="utf-8") as file:
			config.write(file)


do_config = Handleconfig(CONFIG_FILE_PATH)   #创建一个对象方便别的地方调用


if __name__ == '__main__':
	one_config = Handleconfig(CONFIG_FILE_PATH)
	pass
	# print(config())
	# print(config("excel"))
	# print(config("excel","one_res",is_bool=True))
	# print(config("excel", "two_res",is_eval=True))
	# print(config("excel", "three_res",is_bool=True))
	print(one_config("login","url"))


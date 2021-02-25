#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: Handle_context.py
# author:liushen
# time:2021/01/03
# 处理上下文的参数化
import re
from scripts.Handle_mysql_encapsulation import HandleMysql
# from scripts.Do_config import do_config
from scripts.constants import USER_ACCOUNT_FILE_PATH
from scripts.Do_config import Handleconfig
from faker import Faker
import random

# from cases.test_05_invest import LOAN_ID   # 导入模块的时候，如果有多次导入相同的模块，那么只有第一次导入有效
do_config = Handleconfig(USER_ACCOUNT_FILE_PATH)
fk = Faker(locale='zh_CN')


class Context:
    """
    实现参数化，反射功能
    """
    invest_tel_config = do_config('invest_user', 'id')
    not_existed_tel_pattern = re.compile(r"\$\{not_exited_tel\}")  # 创建一个正则表达式
    invest_user_tel_pattern = re.compile(r"\$\{invest_user_tel\}")
    recharge_user_pwd_pattern = re.compile(r"\$\{invest_user_pwd\}")
    loan_id_pattern = re.compile(r"\$\{loan_id\}")
    not_existed_loan_id_pattern = re.compile(r"\$\{not_existed_loan_id\}")
    fullname_pattern = re.compile(r"\$\{fullname\}")
    cardnum_pattern = re.compile(r"\$\{cardnum\}")
    tel_pattern = re.compile(r"\$\{tel\}")
    parenttel_pattern = re.compile(r"\$\{parenttel\}")
    idcard_pattern = re.compile(r"\$\{idcard\}")
    address_pattern = re.compile(r"\$\{address\}")

    @classmethod
    def not_existed_tel_replace(cls, data):
        """
        替换未注册的手机号
        :param data:
        :return:
        """
        do_mysql = HandleMysql()
        if re.search(cls.not_existed_tel_pattern, data):
            not_existed_tel = do_mysql.creat_not_existed_mobile()
            re.sub(cls.not_existed_tel_pattern, not_existed_tel, data)

        do_mysql.mysql_close()  # 创建时就把关闭mysql的方法写好

        return data

    @classmethod
    def invest_user_tel_replace(cls, data):
        """
        替换投资人的手机号
        :param data:
        :return:
        """
        # 这里不需要向数据库发起请求了，我们这里先用正则替换
        if re.search(cls.invest_user_tel_pattern, data):
            # 然后再去配置文件中找已经注册好的投资人信息
            invest_user_tel = str(cls.invest_tel_config("invest_user", "mobilephone"))  # 从配置文件读取的mobilephone是int类型
            data = re.sub(cls.invest_user_tel_pattern, invest_user_tel, data)  # 第二个替换的数据以及第三个data原始数据一定要是字符串
        return data

    @classmethod
    def loan_id_replace(cls, data):
        """
        替换存在和不存在的标ID
        :param data:
        :return:
        """
        # 这里不需要向数据库发起请求了，我们这里先用正则替换
        if re.search(cls.loan_id_pattern, data):
            # 然后再去配置文件中找已经注册好的投资人信息
            # loan_id = str(LOAN_ID)
            # 第一个参数为对象或类，第二个参数为字符串类型的属性名，作用是获取这个对象或者类的实例属性或类属性，如果第一个参数是对象那就获取的是实例属性
            # 如果那边的setattr没有创建运行直接运行这个py文件，会报错，所以我们要在main下面主动手写定义一个例如：Context.loan_id = 36
            loan_id = str(getattr(cls, "loan_id"))
            # setattr和getattr作用是相反的,setattr是给对象或类赋予实例属性或类属性，格式为setattr(object,字符串类型的name,value)，类似于Java中的反射
            data = re.sub(cls.loan_id_pattern, loan_id, data)  # 第二个替换的数据以及第三个data原始数据一定要是字符串

        if re.search(cls.not_existed_loan_id_pattern, data):
            do_mysql = HandleMysql()
            sql = "SELECT MAX(Id) AS total_loan_id FROM future.`loan` LIMIT 0,1;"
            cls.not_existed_loan_id = str(do_mysql(sql=sql)["total_loan_id"] + 1)  # 生成一个数据库最大的loan_id + 1
            data = re.sub(cls.not_existed_loan_id_pattern, cls.not_existed_loan_id, data)
            do_mysql.mysql_close()  # 关闭数据库连接

        return data

    @classmethod
    def invest_user_pwd_replace(cls, data):
        """
        替换投资人的密码
        :param data:
        :return:
        """
        if re.search(cls.recharge_user_pwd_pattern, data):
            invest_user_pwd = str(cls.invest_tel_config("invest_user", "pwd"))
            data = re.sub(cls.recharge_user_pwd_pattern, invest_user_pwd, data)
        return data

    @classmethod
    def fullname_replace(cls, data):
        """
        患者姓名
        :param data:
        :return:
        """
        if re.search(cls.fullname_pattern, data):
            fullname = fk.name()
            data = re.sub(cls.fullname_pattern, fullname, data)
        return data

    @classmethod
    def cardnum_replace(cls, data):
        """
        患者卡号
        :param data:
        :return:
        """
        if re.search(cls.cardnum_pattern, data):
            cardnum = random.randint(1000000000, 9999999999)
            data = re.sub(cls.cardnum_pattern, cardnum, data)
        return data

    @classmethod
    def tel_replace(cls, data):
        """
        患者电话
        :param data:
        :return:
        """
        if re.search(cls.tel_pattern, data):
            tel = fk.phone_number()
            data = re.sub(cls.tel_pattern, tel, data)
        return data

    @classmethod
    def parenttel_replace(cls, data):
        """
        患者亲属电话
        :param data:
        :return:
        """
        if re.search(cls.parenttel_pattern, data):
            parenttel = fk.phone_number()
            data = re.sub(cls.parenttel_pattern, parenttel, data)
        return data

    @classmethod
    def idcard_replace(cls, data):
        """
        患者身份证号
        :param data:
        :return:
        """
        if re.search(cls.idcard_pattern, data):
            idcard = fk.ssn(min_age=18, max_age=90)
            data = re.sub(cls.idcard_pattern, idcard, data)
        return data

    @classmethod
    def address_replace(cls, data):
        """
        患者身份证号
        :param data:
        :return:
        """
        if re.search(cls.address_pattern, data):
            address = fk.address()
            data = re.sub(cls.address_pattern, address, data)
        return data

    @classmethod
    def register_parameterization(cls, data):
        """
        实现注册功能的参数化
        :param data:
        :return:
        """
        # 先替换未注册的手机号
        data = cls.not_existed_tel_replace(data)
        # 再替换已注册的手机号
        data = cls.invest_user_tel_replace(data)

        return data

    @classmethod
    def recharge_parameterization(cls, data):
        """
        实现充值功能参数化
        :param data:
        :return:
        """
        data = cls.invest_user_tel_replace(data)

        data = cls.invest_user_pwd_replace(data)

        return data

    @classmethod
    def invest_parameterization(cls, data):
        """
        实现投资功能参数化
        :param data:
        :return:
        """
        data = cls.loan_id_replace(data)
        return data
        pass

    @classmethod
    def add_patient_parameterization(cls, data):
        data = cls.fullname_replace(data)
        data = cls.cardnum_replace(data)
        data = cls.tel_replace(data)
        data = cls.parenttel_replace(data)
        data = cls.idcard_replace(data)
        data = cls.address_replace(data)

        return data


if __name__ == '__main__':
    Context.loan_id = 36

    target_str1 = '{"mobilephone":"${not_exited_tel}","pwd":"123456","regname":"静宝"}'
    target_str2 = '{"mobilephone":"${not_exited_tel}","pwd":"123456"，"regname":""}'
    target_str3 = '{"mobilephone":"","pwd":"123456",}'
    target_str4 = '{"mobilephone":"18000001212","pwd":""}'
    three_invest_data = '{"id":"${loan_id}","status":4}'

    print(Context.invest_parameterization(three_invest_data))
    print(Context.register_parameterization(target_str1))
    print(Context.register_parameterization(target_str2))
    print(Context.register_parameterization(target_str3))
    print(Context.register_parameterization(target_str4))

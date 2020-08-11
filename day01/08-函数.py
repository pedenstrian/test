#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : nick
# @Site    : http://www.isscollege.com/

# 函数：复用代码, 封装功能
# 定义函数
"""
def:定义方法的关键字
my_sum：方法名的作用是后续通过方法名称来调用此方法
a, b是形式参数
return:返回
"""
def my_sum(a, b):  # a, b是形式参数
    """
    加法
    :param a:数1
    :param b:数2
    :return:数1加数2的和
    """
    result = a + b
    # return # 默认返回None
    return result# 碰到return就会终止函数
    # print('aaaa')


a = my_sum(1.1, 2.1)  # 1, 2是实际参数
print(a)



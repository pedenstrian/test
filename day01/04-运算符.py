#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : nick
# @Site    : http://www.isscollege.com/

# 除法: /  //
print(4/3)  # 保留小数1.3333333333333333
print(4//3)  # 整除1

# % 求余、取模
print(4 % 3)  # 余数：1


print(2 ** 2)  # 4

# 赋值运算符
# a = 1, b = 2, 交换a和b的值
a = 1
b = 2
a, b = b, a  # 交换a和b的值
print(a, ',', b)


# 逻辑运算符
b1 = True
b2 = False
print(b1 or b2)  # True
print(b1 and b2)  # False
print(not b1)  # False


print(1 + 2 + b1)  # 4
print(1 + 2 + b2)  # 3


print('*********************************************')
print('*' * 40)  # 字符串支持和整数的乘法,其它不支持
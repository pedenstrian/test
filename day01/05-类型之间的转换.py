#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : nick
# @Site    : http://www.isscollege.com/

# 计算器              CTRL+/   单行注释的快捷键
# num1 = input('请输入第一个数字:\n')
# num2 = input('请输入第二个数字:\n')
# # print(num1, '+', num2, '=', (int(num1) + int(num2)))
# print(num1, '+', num2, '=', (float(num1) + float(num2)))
params = input('请输入:')  # 用户输入一个危险的命令
result = eval(params)  # eval命令谨慎使用
print(result)  # 2

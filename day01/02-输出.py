#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : nick
# @Site    : http://www.isscollege.com/

print('hello world')

name = 'nick'
age = 30
height = 1.8
married = True  # False
# 输出nick的信息
print('姓名:', name, ",年龄:", age, ',身高:', height, ',结婚:', married)
# 主流方式
print('姓名:%s' % name)
# 传入的值和占位符的类型要一一对应,有一个例外:任意类型都可以传值给字符串占位符
print('姓名:%s, 年龄:%d, 身高:%.2f, 结婚:%s' % (name, age, height, married))
# print是默认输出后换行,如果不想换行则使用end参数
print('第一行', end=',')
print('第一行')  # 第一行,第一行

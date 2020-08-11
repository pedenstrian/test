#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : nick
# @Site    : http://www.isscollege.com/
# 顺序结构

# print('---begin----')
# print('---content----')


# 分支:选择
# raining = True
#
# if raining:
#     print('宅在家里')
# else:
#     print('出去玩耍')
# print('---end----')

# 根据输入的分数给出评级

# num_str = input("请输入一个分数")
# num = float(num_str)
# # 分数100-85 优秀
# if num > 100 or num < 0:
#     print('输入不合法')
# elif num >=85:
#     print('优秀')
# elif num >= 75:
#     print('良好')
# elif  num >= 60:
#     print('及格')
# else:
#     print('不及格')

# python里面没有switch case语句
# 三目运算符   java:   布尔表达式 ? 表达式2:表达式3
# 如果if后的表达式3<2返回True, 那么表达式1 if 3<2 else 2的值就是1,否则就是else后的值2
# result = 1 if 3<2 else 2
# print(result)


# 获取用户名
# username = input("请输入用户名:\n")
# # 获取密码
# password = input("请输入密码:\n")
#
# if (username == "admin" or username == "user") and password == "8888":
#     if username == "admin":
#         print("欢迎管理员登录")
#     else:
#         print("欢迎用户登录")
# else:
#     if username != "admin" and username != "user":
#         if password != "8888":
#             print("用户名和密码错误")
#         else:
#             print("用户名错误")
#     else:
#         print("密码错误")

# 循环
# while
# 定义变量接收结果
sum1 = 0
# 定义一个变量i
i = 0
# 0-100的偶数和
# while i <= 100:
#     if i%2 == 0:
#         sum1 += i  # sum1 = sum1 + i
#     i += 1  # python里面没有i++
# print(sum1)  # 5050

# while循环嵌套:打印直角三角形
# j = 0
# while j < 5:
#     k = 0
#     while k <= j:
#         print("*", end=' ')
#         k += 1
#     print('')
#     j += 1

# for:一般用于固定次数的循环
# for i in range(10): # [0, 10)
#     print(i)
# for i in range(1, 11): # [1, 11)
#     print(i)
# for i in range(1, 11, 2): # [1, 11), 2代表步进,每次增加2
#     print(i)
# str1 = 'abcdefg'
# for s in str1:
#     print(s)

# for i in range(10):
#     a = 1/0
#     print(i)
# else:  # for循环执行结束后会执行else语句,如果for循环中出现异常,不会执行else
#     print('else')

# break:终止最内层的循环
# for i in range(10):
#     for j in range(5):
#         if j > 3:
#             break
#         print(i, ' ', j)


# for i in range(10):
#     if i%2 ==0:
#         continue  # 跳过当前循环后面的代码
#     print(i)




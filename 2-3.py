#!/usr/bin/python  
# -*- coding: utf-8 -*-  
#coding=utf-8
import math
def  funtion(x,y,f):
	return f(x) + f(y)
print funtion(-2,-9,abs)

a = 'SdfdG'
print '-----------------'
print a.upper()  
print '++++++++++++++++++++'

#map函数的语法如下
#map()函数接受的方式：一个函数和一个list，如下例子。
def name(s):
	return s[0].upper() + s[1:].lower()
print map(name,['adam', 'LISA', 'barT'])

#reduce()函数也是Python内置的一个高阶函数。
#reduce()函数接收的参数和 map()类似，一个函数 f，
#一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。
#例如，编写一个f函数，接收x和y，返回x和y的和：
def prod(x, y):
    return x * y

print reduce(prod, [2, 4, 5, 7, 12])
#reduce函数同时也能用于加法和减法等运算

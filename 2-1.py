#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2022/05/18 15:43:57
# @Author  : dch0319
# @File    : 2-1.py
# @Software: Visual Studio Code
import math


def fun(x):
    return math.exp(x) + x - 7


def _fun(x):
    return math.exp(x) + 1


def binary(a, b):
    while (b - a) / 2 > 0.5 * 10**(-8):
        c = (a + b) / 2
        if fun(c) == 0:
            break
        if fun(a) * fun(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


def fixedPoint(a, b):
    x = (a + b) / 2
    x_list = [x]
    while True:
        x = math.log(7 - x)
        x_list.append(x)
        error = abs(x_list[-1] - x_list[-2])
        if error < 0.5 * 10**(-8):
            break
    return x_list[-1]


def newton(a):
    x = a
    x_list = [x]
    while True:
        x = x - fun(x) / _fun(x)
        x_list.append(x)
        error = abs(x_list[-1] - x_list[-2])
        if error < 0.5 * 10**(-8):
            break
    return x_list[-1]


def shiwei(a, b):
    c_list = [a]
    while True:
        c = (b * fun(a) - a * fun(b)) / (fun(a) - fun(b))
        if fun(c) == 0:
            break
        if fun(a) * fun(c) < 0:
            b = c
        else:
            a = c
        c_list.append(c)
        error = abs(c_list[-1] - c_list[-2])
        if error < 0.5 * 10**(-8):
            break
    return c_list[-1]


a = 1.5
b = 2
print("⼆分法:", binary(a, b))
print("不动点法:", fixedPoint(a, b))
print("⽜顿法:", newton(a))
print("试位法:", shiwei(a, b))

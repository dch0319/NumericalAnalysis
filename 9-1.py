#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2022/05/15 20:37:59
# @Author  : dch0319
# @File    : 7-1.py
# @Software: Visual Studio Code

import numpy as np


def fun(x):
    return np.exp(x)


def fun2(x, h):
    return (fun(x - 2 * h) - 4 * fun(x - h) + 3 * fun(x)) / (2 * h)


def fun3(x, h):
    return (-fun(x + 2 * h) + 16 * fun(x + h) - 30 * fun(x) + 16 * fun(x - h) -
            fun(x - 2 * h)) / (12 * h**2)


h = np.logspace(-1, -9, 9)
x = 0
y_1 = np.zeros(9)
e_1 = np.zeros(9)
y_2 = np.zeros(9)
e_2 = np.zeros(9)

for i in range(len(h)):
    y_1[i] = fun2(x, h[i])
    e_1[i] = y_1[i] - 1
print('一阶导数{}'.format(y_1))
print('误差{}'.format(e_1))
for i in range(len(h)):
    y_2[i] = fun3(x, h[i])
    e_2[i] = y_2[i] - 1
print('二阶导数{}'.format(y_2))
print('误差{}'.format(e_2))

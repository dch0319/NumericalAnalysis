#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2022/5/1 11:58
# @Author  : dch0319
# @File    : 6-2.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import math


def chaZhiBiao(X, Y):
    n = len(x)
    A = np.zeros([n, n])
    for i in range(n):
        A[i][0] = Y[i]
    for j in range(1, n):
        for i in range(j, n):
            A[i][j] = (A[i][j - 1] - A[i - 1][j - 1]) / (X[i] - X[i - j])
    return A


def Newton(A, x, t):
    res = np.zeros_like(t)
    for k in range(len(t)):
        n = len(x)
        sum = 0
        for i in range(n):
            r = A[i][i]
            for j in range(i):
                r *= t[k] - x[j]
            sum += r
        res[k] = sum
    return res


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
n = 31
x = np.linspace(-2, 2, n)
y = 1 / (1 + 12 * x ** 2)
A = chaZhiBiao(x, y)
t = np.linspace(-2, 2, 1000)
f = Newton(A, x, t)
f2 = 1 / (1 + 12 * t ** 2)
x = np.zeros_like(x)
for i in range(n):
    x[i] = 2 * math.cos((2 * i + 1) / (2 * n) * math.pi)
y = 1 / (1 + 12 * x ** 2)
A = chaZhiBiao(x, y)
f3 = Newton(A, x, t)
plt.title('插值节点数:{}'.format(n))
plt.plot(t, f, label='均匀插值')
plt.plot(t, f2, label='实际函数')
plt.plot(t, f3, label='切比雪夫插值')
plt.legend()
plt.show()

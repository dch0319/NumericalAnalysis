#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2022/5/1 11:58
# @Author  : dch0319
# @File    : 6-1.py
# @Software: PyCharm

import numpy as np
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
    n = len(x)
    sum = 0
    for i in range(n):
        r = A[i][i]
        for j in range(i):
            r *= t - x[j]
        sum += r
    return sum


x = np.array([0, math.pi / 6, math.pi / 3, math.pi / 4, math.pi / 2])
y = np.sin(x)
A = chaZhiBiao(x, y)
t = [1, math.pi - 2, math.pi - 3, 4 - math.pi,
     14 - 4 * math.pi, 1000 - 318 * math.pi]
for i in range(len(t)):
    f = Newton(A, x, t[i])
    print('{}的估计值:{}'.format(t[i], f))
    print('{}的实际值:{}'.format(t[i], math.sin(t[i])))
    print('误差:{}'.format(abs(f - math.sin(t[i]))))

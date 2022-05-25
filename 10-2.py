#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2022/05/23 22:44:30
# @Author  : dch0319
# @File    : 10-2.py
# @Software: Visual Studio Code

import numpy as np


def fun(x):
    return x * np.exp(x)


def romberg(a, b, n):
    r = np.zeros((n, n))
    h = (b - a) / (2**np.arange(0, n))
    r[0, 0] = (b - a) * (fun(a) + fun(b)) / 2
    for j in range(2, n + 1):
        subtotal = 0
        for i in range(1, 2**(j - 2) + 1):
            subtotal += fun(a + (2 * i - 1) * h[j - 1])
        r[j - 1, 0] = r[j - 2, 0] / 2 + h[j - 1] * subtotal
        for k in range(2, j + 1):
            r[j - 1, k - 1] = (4**(k - 1) * r[j - 1, k - 2] -
                               r[j - 2, k - 2]) / ((4**(k - 1) - 1))
    print('R=\n{}'.format(r))

    err = r
    for k in range(n):
        for l in range(k+1):
            err[k, l] -= 1

    print('error=\n{}'.format(err))


romberg(0, 1, 5)

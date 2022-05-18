#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2022/5/10 19:38
# @Author  : dch0319
# @File    : 6-3.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import solve


def cubic_spline_interp(x_val, y_val, x_interp):
    x_lst = [x_interp] if isinstance(x_interp, (float, int)) else x_interp
    x_loc = np.searchsorted(x_val, x_lst)
    p, q = chashang(x_val, y_val)
    n = len(x_val) - 1
    h_vec = x_val[1:] - x_val[:-1]
    _u_vec = h_vec[-1:] / (h_vec[:-1] + h_vec[1:])
    u_vec = _u_vec[1:]
    lam_vec = 1 - u_vec
    diag_mat = np.diag(u_vec, k=-1) + np.diag([2] * (n - 1)) + np.diag(lam_vec, k=1)
    d_vec = 6 * p[2:, 3]
    m_vec = np.insert(np.append(solve(diag_mat, d_vec), 0), 0, 0)
    res_lst = []
    for x, i in zip(x_lst, x_loc):
        h_i = x_val[i] - x_val[i - 1]
        S_i = m_vec[i - 1] * (x_val[i] - x) ** 3 / (6 * h_i) + m_vec[i] * (x - x_val[i - 1]) ** 3 / (6 * h_i) + \
              (y_val[i - 1] - 1 / 6 * m_vec[i - 1] * h_i ** 2) * (x_val[i] - x) / h_i + \
              (y_val[i] - 1 / 6 * m_vec[i] * h_i ** 2) * (x - x_val[i - 1]) / h_i
        res_lst.append(S_i)

    return res_lst


def chashang(x, y):
    n = len(x)
    p = np.zeros((n, n + 1))
    p[:, 0] = x
    p[:, 1] = y
    for j in range(2, n + 1):
        p[j - 1: n, j] = (p[j - 1: n, j - 1] - p[j - 2: n - 1, j - 1]) / (x[j - 1: n] - x[: n + 1 - j])
    q = np.diag(p, k=1)
    return p, q


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
f3 = cubic_spline_interp(x, y, t)
plt.title('插值节点数:{}'.format(n))
plt.plot(t, f, label='牛顿插值')
plt.plot(t, f2, label='实际函数')
plt.plot(t, f3, label='自然三次样条插值')
plt.legend()
plt.show()

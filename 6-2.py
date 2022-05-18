#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2022/05/18 15:59:01
# @Author  : dch0319
# @File    : 6-2.py
# @Software: Visual Studio Code
import numpy as np


def myQR(A):
    (r, c) = np.shape(A)
    Q = np.identity(r)
    R = np.copy(A)
    for cnt in range(r - 1):
        x = R[cnt:, cnt]
        e = np.zeros_like(x)
        e[0] = np.linalg.norm(x)
        u = x - e
        v = u / np.linalg.norm(u)
        Q_cnt = np.identity(r)
        Q_cnt[cnt:, cnt:] -= 2.0 * np.outer(v, v)
        R = np.dot(Q_cnt, R)  # R=H(n-1)*...*H(2)*H(1)*A
        Q = np.dot(Q, Q_cnt)  # Q=H(n-1)*...*H(2)*H(1) H为⾃逆矩阵
    return (Q, R)


a = np.array([[8, -8, -4], [12, -15, -7], [-18, 26, 12]])
for k in range(25):
    (q, r) = myQR(a)
    a = r @ q
print("25次迭代后特征值为:", a.diagonal(0))
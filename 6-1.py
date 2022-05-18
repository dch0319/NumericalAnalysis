#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2022/05/18 15:56:51
# @Author  : dch0319
# @File    : 6-1.py
# @Software: Visual Studio Code
import numpy as np


def powerit(A, x, k):
    A = np.array(A, dtype=np.float64)
    x1 = np.array(x, dtype=np.float64)
    x2 = np.array(x, dtype=np.float64)
    r_list = [np.linalg.norm(x1)]
    for _ in range(k):
        u1 = x1 / np.linalg.norm(x1)
        x1 = A @ u1
        lam1 = u1.T @ x1
        r_list.append(np.linalg.norm(x1))
    u1 = x1 / np.linalg.norm(x1)
    s_list = []
    for i in range(len(r_list) - 2):
        s = (r_list[i] * r_list[i + 2] - r_list[i + 1]**2) / (
            r_list[i] - 2 * r_list[i + 1] + r_list[i + 2])
        s_list.append(s)
    for i in range(k - 2):
        u2 = x2 / s_list[i]
        x2 = A @ u2
    lam2 = s_list[-1]
    u2 = x2 / np.linalg.norm(x2)
    return lam1, u1, lam2, u2


def invpowerit(A, x, k):
    A = np.array(A, dtype=np.float64)
    x1 = np.array(x, dtype=np.float64)
    x2 = np.array(x, dtype=np.float64)
    r_list = [np.linalg.norm(x1)]
    for _ in range(k):
        u1 = x1 / np.linalg.norm(x1)
        x1 = np.linalg.inv(A) @ u1
        lam1 = u1.T @ x1
        r_list.append(np.linalg.norm(x1))
    u1 = x1 / np.linalg.norm(x1)
    s_list = []
    for i in range(len(r_list) - 2):
        s = (r_list[i] * r_list[i + 2] - r_list[i + 1]**2) / (
            r_list[i] - 2 * r_list[i + 1] + r_list[i + 2])
        s_list.append(s)
    for i in range(k - 2):
        u2 = x2 / s_list[i]
        x2 = np.linalg.inv(A) @ u2
    lam2 = -s_list[-1]
    u2 = x2 / np.linalg.norm(x2)
    return lam1, u1, lam2, u2


A = [[8, -8, -4], [12, -15, -7], [-18, 26, 12]]
x = [[1], [1], [1]]
lam1, u1, lam2, u2 = powerit(A, x, 12)
print("模最⼤特征值:", lam1[0][0])
print("对应特征向量", u1)
print("加速后:")
print("模最⼤特征值:", lam2)
print("对应特征向量", u2)
lam1, u1, lam2, u2 = invpowerit(A, x, 12)
print("模最⼩特征值:", lam1[0][0])
print("对应特征向量", u1)
print("加速后:")
print("模最⼩特征值:", lam2)
print("对应特征向量", u2)
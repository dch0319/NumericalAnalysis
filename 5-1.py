#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2022/05/18 15:54:34
# @Author  : dch0319
# @File    : 5-1.py
# @Software: Visual Studio Code
import numpy as np


def TiDuXiaJiang(A, b):
    A = np.array(A, dtype=np.float64)
    dim = A.shape[0]
    b = np.array(b, dtype=np.float64)
    x = np.zeros((dim, 1))
    v = b - A @ x
    x_list = [x]
    while True:
        w = A @ v
        t = (v.T @ v) / (v.T @ w)
        x = x + t * v
        v = v - t * w
        x_list.append(x)
        if abs(x_list[-1] - x_list[-2]).max() < 0.5 * 10**(-8):
            break
    print("梯度下降： ")
    print(x_list[-1])
    return x_list[-1]


def GongETiDu(A, b):
    A = np.array(A, dtype=np.float64)
    dim = A.shape[0]
    b = np.array(b, dtype=np.float64)
    x = np.zeros((dim, 1))
    v = r = b - A @ x
    rr0 = r.T @ r
    x_list = [x]
    while True:
        w = A @ v
        t = rr0 / (v.T @ w)
        x = x + t * v
        r = r - t * w
        rr1 = r.T @ r
        s = rr1 / rr0
        rr0 = rr1
        v = r + s * v
        x_list.append(x)
        if abs(x_list[-1] - x_list[-2]).max() < 0.5 * 10**(-8):
            break
    print("共轭梯度： ")
    print(x_list[-1])
    return x_list[-1]


A = [[4, -2, 0], [-2, 2, -1], [0, -1, 5]]
b = [[0], [3], [-7]]
TiDuXiaJiang(A, b)
GongETiDu(A, b)
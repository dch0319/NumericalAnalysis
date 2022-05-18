#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2022/05/18 15:48:06
# @Author  : dch0319
# @File    : 3-1.py
# @Software: Visual Studio Code
import numpy as np


def gauss(A, b):
    A = np.array(A, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    row = A.shape[0]  # ⾏数
    column = A.shape[1]  # 列数
    # 消元
    for i in range(row - 1):
        # 找出列中绝对值最⼤元素，作⾏变换，让绝对值最⼤的元素⾏作主元
        temp = []
        for j in range(i, row):
            temp.append(A[j][i])
        num = temp.index(max(temp)) + i
        A[[num, i], :] = A[[i, num], :]
        b[[num, i], :] = b[[i, num], :]
        for j in range(i + 1, row):
            beishu = A[j][i] / A[i][i]
            for k in range(i, column):
                A[j][k] = A[j][k] - beishu * A[i][k]
            b[j] = b[j] - beishu * b[i]
    # 回代
    x = [0] * column
    x[column - 1] = b[column - 1] / A[column - 1][column - 1]
    for i in range(row - 2, -1, -1):
        for j in range(column - 1, i, -1):
            b[i] = b[i] - A[i][j] * x[j]
        x[i] = b[i] / A[i][i]
    print("⾼斯消元法： ")
    for i in range(column):
        print("x{} =".format(i + 1), '%.12f' % x[i])
    return x


def LU(A, b):
    A = np.array(A, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    L = np.zeros_like(A)
    row = A.shape[0]
    P = np.identity(row)
    for i in range(row - 1):
        # 绝对值最⼤元素所在的⾏数
        index = i + np.argmax(abs(A[i:, i]))
        # 交换A， L， P的⾏
        if index != i & index != row - 1:
            A[[i, index], :] = A[[index, i], :]
            L[[i, index], :] = L[[index, i], :]
            P[[i, index], :] = P[[index, i], :]
        L[i, i] = 1
        for j in range(i + 1, row):
            L[j, i] = A[j, i] / A[i, i]
            A[j, :] = A[j, :] - L[j, i] * A[i, :]
    L[i + 1, i + 1] = 1
    U = np.array(A)
    c = np.linalg.inv(L) @ P @ b
    x = np.linalg.inv(U) @ c
    print("LU分解法： ")
    for i in range(row):
        print("x{} =".format(i + 1), '%.12f' % x[i])
    return x


A = [[3, 1, 2], [6, 3, 4], [3, 2, 5]]
b = [[11], [24], [22]]
gauss(A, b)
LU(A, b)
H12 = 1. / (np.arange(1, 13) + np.arange(0, 12)[:, np.newaxis])
b = H12 @ np.ones((12, 1))
gauss(H12, b)
LU(H12, b)
H20 = 1. / (np.arange(1, 21) + np.arange(0, 20)[:, np.newaxis])
b = H20 @ np.ones((20, 1))
gauss(H20, b)
LU(H20, b)
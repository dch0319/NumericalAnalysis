#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2022/05/18 15:52:41
# @Author  : dch0319
# @File    : 4-1.py
# @Software: Visual Studio Code
import numpy as np


def Jacobi(A, b):
    A = np.array(A, dtype=np.float64)
    dim = A.shape[0]
    b = np.array(b, dtype=np.float64)
    D = np.diag(np.diagonal(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    x = np.zeros((dim, 1))
    x_list = [x]
    while True:
        x = np.linalg.inv(D) @ (b - (L + U) @ x)
        x_list.append(x)
        if (x_list[-1] - x_list[-2]).max() < 0.5 * 10**(-6):
            break
    print("Jacobi迭代： ")
    print(x_list[-1])
    return x_list[-1]


def GS(A, b):
    A = np.array(A, dtype=np.float64)
    dim = A.shape[0]
    b = np.array(b, dtype=np.float64)
    D = np.diag(np.diagonal(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    x = np.zeros((dim, 1))
    x_list = [x]
    while True:
        x = np.linalg.inv(D + L) @ (b - U @ x)
        x_list.append(x)
        if (x_list[-1] - x_list[-2]).max() < 0.5 * 10**(-6):
            break
    print("GS迭代： ")
    print(x_list[-1])
    return x_list[-1]


def SOR(A, b):
    omega = 1.1
    A = np.array(A, dtype=np.float64)
    dim = A.shape[0]
    b = np.array(b, dtype=np.float64)
    D = np.diag(np.diagonal(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    x = np.zeros((dim, 1))
    x_list = [x]
    while True:
        x = np.linalg.inv(D + omega * L) @ (
            (1 - omega) * D @ x -
            omega * U @ x) + omega * np.linalg.inv(D + omega * L) @ b
        x_list.append(x)
        if (x_list[-1] - x_list[-2]).max() < 0.5 * 10**(-6):
            break
    print("SOR迭代： ")
    print(x_list[-1])
    return x_list[-1]


A = [[3, -1, 1], [1, -8, -2], [1, 1, 5]]
b = [[-2], [1], [4]]
Jacobi(A, b)
GS(A, b)
SOR(A, b)
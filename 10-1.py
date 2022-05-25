#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2022/05/23 21:22:25
# @Author  : dch0319
# @File    : 10-1.py
# @Software: Visual Studio Code

import numpy as np


def fun(x):
    return x * np.exp(x)


def fun2(x1, x2, t):
    temp = 0.5*(t*(x2-x1)+x2+x1)
    return (temp)*np.exp(temp)*(x2-x1)*0.5


def fu_he_zhong_xin(real, n):
    for i in range(len(n)):
        x = np.linspace(1 / (2 * n[i]), 1 - 1 / (2 * n[i]), n[i])
        f = fun(x)
        v = np.sum(f) / n[i]
        err = v - real
        print('复合中心法则取{}个子区间时计算误差={}'.format(n[i], err))


def fu_he_ti_xing(real, n):
    for i in range(len(n)):
        h = 1 / n[i]
        x = np.arange(0, 1 + h, h)
        f = fun(x)
        a = np.block([1 / 2, np.ones(n[i] - 1), 1 / 2])
        q = np.sum(a * f) * h
        err = q - real
        print('复合梯形法则取{}个子区间时计算误差={}'.format(n[i], err))


def fu_he_xin_pu_sen(real, n):
    for i in range(len(n)):
        h = 1 / n[i]
        x = np.arange(0, 1 + h, h)
        f = fun(x)
        a = np.ones((1, n[i] + 1))
        a[0, 1:-1:2] = 4
        a[0, 2:-1:2] = 2
        q = np.sum(a * f) * h / 3
        err = q - real
        print('复合辛普森法则取{}个子区间时计算误差={}'.format(n[i], err))


def fu_he_san_dian_gauss(real, n):
    for i in range(len(n)):
        h = 1 / n[i]
        x = np.arange(0, 1 + h, h)
        v = 0
        for j in range(n[i]):
            v += 8/9*fun2(x[j], x[j+1], 0)+5/9*fun2(x[j],
                                                    x[j+1], 0.6**0.5)+5/9*fun2(x[j], x[j+1], -0.6**0.5)
        err = v-real
        print('复合三点高斯积分取{}个子区间时计算误差={}'.format(n[i], err))


real = 1
n = np.array([1, 2, 4, 8, 16, 32])
fu_he_zhong_xin(real, n)
fu_he_ti_xing(real, n)
fu_he_xin_pu_sen(real, n)
fu_he_san_dian_gauss(real, n)

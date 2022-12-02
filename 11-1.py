#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2022/06/17 17:05:22
# @Author  : dch0319
# @File    : 11-1.py
# @Software: Visual Studio Code

import numpy as np


def mathy(t):
    return 1-1/((1/9)*np.exp(t)+1)


def fun(y):
    return y*(1-y)


def elfun(t, h, y0):
    y = np.zeros_like(t)
    y[0] = y0
    for i in range(len(t)-1):
        y[i+1] = y[i]+h*fun(y[i])
    return y


def txfun(t, h, y0):
    y = np.zeros_like(t)
    y[0] = y0
    for i in range(len(t)-1):
        y[i+1] = y[i]+h/2*(fun(y[i])+fun(y[i]+h*fun(y[i])))
    return y


def rk3(t, h, y0):
    y = np.zeros_like(t)
    y[0] = y0
    for i in range(len(t)-1):
        k1 = fun(y[i])
        k2 = fun(y[i]+1/2*h*k1)
        k3 = fun(y[i]+3/4*h*k2)
        y[i+1] = y[i]+h/9*(2*k1+3*k2+4*k3)
    return y


def rk4(t, h, y0):
    y = np.zeros_like(t)
    y[0] = y0
    for i in range(len(t)-1):
        k1 = fun(y[i])
        k2 = fun(y[i]+1/3*h*k1)
        k3 = fun(y[i]-1/3*h*k1+h*k2)
        k4 = fun(y[i]+h*k1-h*k2+h*k3)
        y[i+1] = y[i]+h/8*(k1+3*k2+3*k3+k4)
    return y


h1 = 0.1
h2 = 0.05
y0 = 0.1
t1 = np.arange(0, 2+h1, h1)
t2 = np.arange(0, 2+h2, h2)
y_real_h1 = np.zeros_like(t1)
y_real_h2 = np.zeros_like(t2)
for i in range(len(t1)):
    y_real_h1[i] = mathy(t1[i])
for i in range(len(t2)):
    y_real_h2[i] = mathy(t2[i])

y = elfun(t1, h1, y0)
e = y-y_real_h1
print("显式欧拉法,h=0.1,结果:\n{}\n误差:\n{}".format(y, e))

y = elfun(t2, h2, y0)
e = y-y_real_h2
print("显式欧拉法,h=0.05,结果:\n{}\n误差:\n{}".format(y, e))

y = txfun(t1, h1, y0)
e = y-y_real_h1
print("显式梯形法,h=0.1,结果:\n{}\n误差:\n{}".format(y, e))

y = txfun(t2, h2, y0)
e = y-y_real_h2
print("显式梯形法,h=0.05,结果:\n{}\n误差:\n{}".format(y, e))

y = rk3(t1, h1, y0)
e = y-y_real_h1
print("RK3法,h=0.1,结果:\n{}\n误差:\n{}".format(y, e))

y = rk3(t2, h2, y0)
e = y-y_real_h2
print("RK3法,h=0.05,结果:\n{}\n误差:\n{}".format(y, e))

y = rk4(t1, h1, y0)
e = y-y_real_h1
print("RK4法,h=0.1,结果:\n{}\n误差:\n{}".format(y, e))

y = rk4(t2, h2, y0)
e = y-y_real_h2
print("RK4法,h=0.05,结果:\n{}\n误差:\n{}".format(y, e))

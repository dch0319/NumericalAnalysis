#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2022/06/17 17:39:08
# @Author  : dch0319
# @File    : 11-2.py
# @Software: Visual Studio Code

import numpy as np


def fun(a):
    s = 10
    r = 28
    b = 8/3
    x = a[0]
    y = a[1]
    z = a[2]
    dx = -s*x+s*y
    dy = -x*z+r*x-y
    dz = x*y-b*z
    res = np.block([dx, dy, dz])
    return res


x0 = 1
y0 = 1
z0 = 1
h1 = 0.001
h2 = 0.002
t1 = np.arange(0, 80+h1, h1)
t2 = np.arange(0, 80+h2, h2)
x = np.zeros_like(t1)
y = np.zeros_like(t1)
z = np.zeros_like(t1)
x[0] = x0
y[0] = y0
z[0] = z0
# rk3_h1
for i in range(len(t1)-1):
    a = np.block([x[i], y[i], z[i]])
    K1 = fun(a)
    K2 = fun(a+h1*K1)
    K3 = fun(a+h1/4*K1+h1/4*K2)
    s = a+h1/6*(K1+K2+4*K3)
    x[i+1] = s[0]
    y[i+1] = s[1]
    z[i+1] = s[2]
x_rk3_h1 = x[len(t1)-1]
y_rk3_h1 = y[len(t1)-1]
z_rk3_h1 = z[len(t1)-1]
# rk3_h2
for i in range(len(t2)-1):
    a = np.block([x[i], y[i], z[i]])
    K1 = fun(a)
    K2 = fun(a+h2*K1)
    K3 = fun(a+h2/4*K1+h2/4*K2)
    s = a+h2/6*(K1+K2+4*K3)
    x[i+1] = s[0]
    y[i+1] = s[1]
    z[i+1] = s[2]
x_rk3_h2 = x[len(t2)-1]
y_rk3_h2 = y[len(t2)-1]
z_rk3_h2 = z[len(t2)-1]
# rk4_h1
for i in range(len(t1)-1):
    a = np.block([x[i], y[i], z[i]])
    K1 = fun(a)
    K2 = fun(a+1/2*h1*K1)
    K3 = fun(a+h1/2*K2)
    K4 = fun(a+h1*K3)
    s = a+h1/6*(K1+2*K2+2*K3+K4)
    x[i+1] = s[0]
    y[i+1] = s[1]
    z[i+1] = s[2]
x_rk4_h1 = x[len(t1)-1]
y_rk4_h1 = y[len(t1)-1]
z_rk4_h1 = z[len(t1)-1]
# rk4_h2
for i in range(len(t2)-1):
    a = np.block([x[i], y[i], z[i]])
    K1 = fun(a)
    K2 = fun(a+1/2*h2*K1)
    K3 = fun(a+h2/2*K2)
    K4 = fun(a+h2*K3)
    s = a+h2/6*(K1+2*K2+2*K3+K4)
    x[i+1] = s[0]
    y[i+1] = s[1]
    z[i+1] = s[2]
x_rk4_h2 = x[len(t2)-1]
y_rk4_h2 = y[len(t2)-1]
z_rk4_h2 = z[len(t2)-1]

print("RK3 h=0.001\n{}\n{}\n{}".format(x_rk3_h1, y_rk3_h1, z_rk3_h1))
print("RK3 h=0.002\n{}\n{}\n{}".format(x_rk3_h2, y_rk3_h2, z_rk3_h2))
print("RK4 h=0.001\n{}\n{}\n{}".format(x_rk4_h1, y_rk4_h1, z_rk4_h1))
print("RK4 h=0.002\n{}\n{}\n{}".format(x_rk4_h2, y_rk4_h2, z_rk4_h2))

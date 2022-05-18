#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2022/05/18 16:02:53
# @Author  : dch0319
# @File    : 8-1.py
# @Software: Visual Studio Code
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time : 2022/05/15 20:37:59
# @Author : dch0319
# @File : 7-1.py
# @Software: Visual Studio Code
import numpy as np

x = np.linspace(2, 4, 21)
A = np.vander(x, 11, increasing=True)
y = 1 + x + x**2 + x**3 + x**4 + x**5 + x**6 + x**7 + x**8 + x**9 + x**10
q, r = np.linalg.qr(A, mode='complete')
b = q.T @ y
c = np.linalg.solve(r[0:11, 0:11], b[0:11])
print(c)
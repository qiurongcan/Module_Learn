'''
@Descripttion: 
@version: 
@encoding: utf-8
@Author: qiurongcan
Date: 2025-08-26 17:02:54
LastEditTime: 2025-08-26 17:09:04
'''



import numpy as np



p0 = np.array([0, 0])
p1 = np.array([1, 3])  
p2 = np.array([4, 2])
p3 = np.array([5, 0])
points = np.array([p0, p1, p2, p3])


def de_casteljau(points, t):

    temp = points.copy()
    n = len(points)
    for r in range(1, n):
        for i in range(n - r):
            temp[i] = (1-t) * temp[i] + t * temp[i+1]

    # 计算出数值
    return temp[0]


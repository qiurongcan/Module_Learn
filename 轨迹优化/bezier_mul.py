'''
@Descripttion: 多点贝塞尔曲线
@version: 
@encoding: utf-8
@Author: qiurongcan
Date: 2025-08-26 15:15:46
LastEditTime: 2025-08-26 16:14:18
'''

import numpy as np
import matplotlib.pyplot as plt


def cubic_bezier(p0, p1, p2, p3, t):
    """
    三次贝塞尔曲线
    """
    return (1-t)**3 * p0 + 3*(1-t)**2 * t * p1 + 3*(1-t) * t**2 * p2 + t**3 * p3


def compute(points, tension=0.5):
    """计算各点切线方向"""
    n = len(points)
    tangents = np.zeros_like(points)

    # 对于内部点
    for i in range(1, n-1):
        tangents[i] = tension * (points[i+1] - points[i-1])

    # 对于端点
    tangents[0] = tension * (points[1] - points[0])
    tangents[-1] = tension * (points[-1] - points[-2])

    return tangents

def compute_control_points(points, tangents):
    """计算每一段的控制点"""
    n = len(points)
    control_points = []
    for i in range(n - 1):
        c1 = points[i] + tangents[i] / 3
        c2 = points[i+1] - tangents[i+1] / 3

        control_points.append((c1, c2))

    return control_points

def interpolate_multiple_points(points, num_segements=20):
    """对多个点进行贝塞尔插值"""
    n = len(points)
    if n < 2:
        return np.array([])
    
    tangents = compute(points)

    control_points = compute_control_points(points, tangents)

    curve = []
    for i in range(n - 1):
        p0 = points[i]
        p1 = control_points[i][0]
        p2 = control_points[i][1]
        p3 = points[i+1]
        t_val = np.linspace(0, 1, num_segements)
        segment = np.array([cubic_bezier(p0, p1, p2, p3, t) for t in t_val])
        curve.append(segment)
    
    return np.vstack(curve),  control_points

points = np.array([
    [0, 0],
    [2, 3],
    [5, 1],
    [7, 4],
    [10, 2]
])
curve, control_points = interpolate_multiple_points(points)

plt.figure(figsize=(12, 8))
plt.plot(points[: ,0], points[:,1], 'ro-', label="origin", markersize=8)
plt.plot(curve[:,0], curve[:, 1], 'b-', linewidth = 2, label="bezier")

# 绘制控制点和控制线
for i, (c1, c2) in enumerate(control_points):
    plt.plot([points[i][0], c1[0]], [points[i][1], c1[1]], 'g--', alpha=0.7)
    plt.plot([points[i+1][0], c2[0]], [points[i+1][1], c2[1]], 'g--', alpha=0.7)
    plt.scatter([c1[0], c2[0]], [c1[1], c2[1]], c='green', s=50, marker='s')

plt.grid(True, alpha = 0.3)
plt.axis('equal')
plt.legend()
plt.show()






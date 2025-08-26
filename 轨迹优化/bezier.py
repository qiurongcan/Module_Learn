# 贝塞尔曲线


import numpy as np
import matplotlib.pyplot as plt


import numpy as np
import matplotlib.pyplot as plt

def cubic_bezier(p0, p1, p2, p3, t):
    """
    计算三次贝塞尔曲线上的点
    """
    return (1-t)**3 * p0 + 3*(1-t)**2*t * p1 + 3*(1-t)*t**2 * p2 + t**3 * p3

def calculate_control_points(p0, p3, tangent_start, tangent_end, alpha, beta):
    """
    根据起点、终点、切线方向和强度计算控制点
    """
    p1 = p0 + (alpha / 3) * tangent_start
    p2 = p3 - (beta / 3) * tangent_end
    return p1, p2

# 给定的参数
p0 = np.array([0, 0])      # 起点
p3 = np.array([10, 0])     # 终点
tangent_start = np.array([4, 3])  # 起点切线方向 (垂直向上)
tangent_end = np.array([2, 2])    # 终点切线方向 (垂直向上)
alpha = 2.0                # 起点切线强度
beta = 2.0                 # 终点切线强度

# 计算控制点
p1, p2 = calculate_control_points(p0, p3, tangent_start, tangent_end, alpha, beta)

print("控制点坐标:")
print(f"P₀ (起点): ({p0[0]:.2f}, {p0[1]:.2f})")
print(f"P₁ (控制点1): ({p1[0]:.2f}, {p1[1]:.2f})")
print(f"P₂ (控制点2): ({p2[0]:.2f}, {p2[1]:.2f})")
print(f"P₃ (终点): ({p3[0]:.2f}, {p3[1]:.2f})")

# 生成曲线上的点
t_values = np.linspace(0, 1, 100)  # 100个参数点
curve_points = np.array([cubic_bezier(p0, p1, p2, p3, t) for t in t_values])

# 绘制图形
plt.figure(figsize=(12, 8))

# 绘制贝塞尔曲线
plt.plot(curve_points[:, 0], curve_points[:, 1], 'b-', linewidth=2, label='贝塞尔曲线')

# 绘制控制点和连线
plt.plot([p0[0], p1[0]], [p0[1], p1[1]], 'r--', alpha=0.7, label='控制线')
plt.plot([p2[0], p3[0]], [p2[1], p3[1]], 'r--', alpha=0.7)

# 绘制控制点
plt.scatter([p0[0], p3[0]], [p0[1], p3[1]], c='green', s=100, marker='o', label='端点 (P₀, P₃)')
plt.scatter([p1[0], p2[0]], [p1[1], p2[1]], c='red', s=80, marker='s', label='控制点 (P₁, P₂)')

# 绘制切线方向指示
plt.arrow(p0[0], p0[1], tangent_start[0], tangent_start[1], 
          head_width=0.3, head_length=0.5, fc='purple', ec='purple', label='起点切线方向')
plt.arrow(p3[0], p3[1], tangent_end[0], tangent_end[1], 
          head_width=0.3, head_length=0.5, fc='orange', ec='orange', label='终点切线方向')

# 设置图形属性
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.xlabel('X坐标')
plt.ylabel('Y坐标')
plt.title('三次贝塞尔曲线插值示例\nP₀=(0,0) 到 P₃=(10,0)，垂直向上切线')
plt.legend()
plt.show()

# 验证曲线端点属性
print("\n验证:")
print(f"曲线起点 B(0): {cubic_bezier(p0, p1, p2, p3, 0)} (应与P₀相同)")
print(f"曲线终点 B(1): {cubic_bezier(p0, p1, p2, p3, 1)} (应与P₃相同)")

# 计算并显示切线方向（数值微分近似）
dt = 0.001
tangent_at_start = (cubic_bezier(p0, p1, p2, p3, dt) - p0) / dt
tangent_at_end = (p3 - cubic_bezier(p0, p1, p2, p3, 1-dt)) / dt

print(f"曲线在起点的切线方向: ({tangent_at_start[0]:.2f}, {tangent_at_start[1]:.2f})")
print(f"曲线在终点的切线方向: ({tangent_at_end[0]:.2f}, {tangent_at_end[1]:.2f})")



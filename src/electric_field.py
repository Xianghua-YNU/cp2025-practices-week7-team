"""
电偶极子电势与电场计算与可视化模板

本模板用于计算和可视化电偶极子的电势分布和电场线。
学生需要完成标有TODO的三个函数实现。
"""

import numpy as np
import matplotlib.pyplot as plt

# 物理常数
k = 8.99e9  # 库仑常数 (N·m²/C²)
q_pos = 1e-9  # 正点电荷量 (C)
q_neg = -1e-9  # 负点电荷量 (C)

# 电荷位置 [x, y] 坐标 (m)
pos_charge_pos = np.array([0.05, 0])  # 正电荷位置
neg_charge_pos = np.array([-0.05, 0])  # 负电荷位置

def calculate_potential(X, Y):
    """
    计算二维空间电势分布
    
    参数:
        X, Y: 二维网格坐标矩阵 (numpy.ndarray)
        
    返回:
        V: 电势值矩阵 (numpy.ndarray)
    """
    
    # TODO 1: 实现电势计算
    r_1 = ((X-pos_charge_pos[0])**2 +(Y-pos_charge_pos[1])**2)**(1/2)
    r_2 = ((X-neg_charge_pos[0])**2 +(Y-neg_charge_pos[1])**2)**(1/2)
    return (k*q_pos)/r_1 + (k*q_neg)/r_2
    # 提示: 计算每个点到正负电荷的距离，应用电势公式
    pass

def calculate_electric_field(V, spacing):
    """
    通过电势梯度计算电场强度
    
    参数:
        V: 电势值矩阵 (numpy.ndarray)
        spacing: 网格间距 (float)
        
    返回:
        Ex, Ey: 电场在x和y方向的分量 (numpy.ndarray, numpy.ndarray)
    """
    Ey, Ex = np.gradient(-V, spacing, spacing)
    return Ex, Ey
    # TODO 2: 实现电场计算
    # 提示: 使用np.gradient计算电势梯度，注意负号和参数顺序
    pass

def main():
    """
    主函数: 计算并可视化电势和电场
    """
    # 创建计算网格
    x = np.linspace(-0.2, 0.2, 100)
    y = np.linspace(-0.2, 0.2, 100)
    X, Y = np.meshgrid(x, y)

    V = calculate_potential(X, Y)
    Ex, Ey = calculate_electric_field(V, x[1]-x[0])

    plt.figure(figsize=(8, 6))
    
    # 修改1: 使用对数间隔的levels
    levels = np.linspace(-500, 500, 20)  # 自定义范围

    
    # 修改2: 添加clim限制颜色范围
    contour = plt.contourf(X, Y, V, levels=levels, cmap='RdBu_r')
    plt.clim(-500, 500)  # 限制颜色范围
    
    plt.colorbar(label='Electric Potential (V)')
    plt.streamplot(X, Y, Ex, Ey, color='k', density=1.2)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Electric Field and Potential of an Electric Dipole')
    plt.plot(pos_charge_pos[0], pos_charge_pos[1], 'ro', label='Positive Charge')
    plt.plot(neg_charge_pos[0], neg_charge_pos[1], 'bo', label='Negative Charge')
    plt.legend()
    plt.axis('equal')
    plt.grid(True)
    plt.show()
    
 

if __name__ == "__main__":
    main()

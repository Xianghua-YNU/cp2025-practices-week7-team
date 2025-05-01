# SymPy 绘图实验报告

## 一、实验信息

- 小组名称：
- 成员：
- 实验日期：

---

## 二、实验目的

- 熟悉SymPy的plot、plot_implicit、和plot3d_parametric_surface函数；
- 掌握曲线、隐函数和参数曲面的绘制方法。

---

## 三、实验内容与方法

分别说明三个问题的具体绘图方法和使用的函数接口。
def problem1():
    x = sp.symbols('x')
    expr = sp.cos(sp.tan(sp.pi * x))
    # TODO: 完成绘图，区间[-1, 1]
    plot(expr, (x, -1, 1), xlabel='x', ylabel='cos(tan(pi*x))',
         title='Problem 1')

# Problem 2: 使用 plot_implicit 绘制隐函数 e^y + cos(x)/x + y = 0
def problem2():
    x, y = sp.symbols('x y')
    expr = sp.exp(y) + sp.cos(x)/x + y
    # TODO: 完成隐函数绘图，选择合适的绘图区间防止除零错误，例如 x 从 0.1 开始
    plot_implicit(expr, (x, -10, 10), (y, -10, 10),xlabel='x', ylabel='y',title='Problem 2',points=500)

# Problem 3: 使用 plot3d_parametric_surface 绘制参数曲面
def problem3():
    s, t = sp.symbols('s t')
    x = sp.exp(-s)*sp.cos(t)
    y = sp.exp(-s)*sp.sin(t)
    z = t
    # TODO: 完成三维参数曲面绘图
    plot3d_parametric_surface(x, y, z, (s, 0, 8), (t, 0, 5*sp.pi),
                              xlabel='x', ylabel='y', zlabel='z',
                              title='Problem 3')
---

## 四、实验结果与分析

### 问题1: 函数曲线 $\cos(\tan(\pi x))$ 绘制结果

*(插入图片或截图并简要分析曲线特点)*
![屏幕截图 2025-04-09 112841](https://github.com/user-attachments/assets/ccdbf628-06ab-46c2-9ab9-c07b8f6c54e2)
当x接近0.5的时候，因为pi*0.5就是pi/2，此时tan(pi*x)会趋向无穷大，所以cos(tan(pi*x))的值会在-1和1之间快速震荡
### 问题2: 隐函数曲线 $e^y + \frac{\cos x}{x} + y = 0$ 绘制结果

*(插入图片或截图并简要分析隐函数曲线特点)*
![屏幕截图 2025-04-09 112846](https://github.com/user-attachments/assets/c7864ebb-dccf-4c7a-8afb-012761675352)
隐函数绘图通常比较复杂，特别是当分母有x时，x=0会有问题，所以用户调整了区间为x在[-10,-0.1]和[0.1,10]。这里需要注意e^y和y的组合可能使得方程在y较大的区域难以满足，可能曲线主要集中在y的某个范围内，比如负值区域，因为e^y增长很快。另外，cos(x)/x在x绝对值较大时趋近于0，所以当x很大时，方程可能近似为e^y + y ≈ 0，这个方程的解可能在y≈-W(1)，其中W是朗伯W函数，解约为-0.567。因此，隐函数可能在x很大时趋近于y≈-0.567的水平线。而在x接近0的区域，cos(x)/x的绝对值会很大，尤其是当x趋近于0时，cos(x)/x会趋向正无穷或负无穷，这可能导致方程的解只在某些特定的x和y范围内存在。因此，隐函数的图像可能在x接近0时出现急剧的变化，或者在两侧有不同的分支。
### 问题3: 参数曲面绘制结果

*(插入图片或截图并简要分析三维曲面的特点)*
![屏幕截图 2025-04-09 112850](https://github.com/user-attachments/assets/93fc0847-a1a6-4636-9d70-8055253ec205)
参数方程为x = e^{-s} cos(t)，y = e^{-s} sin(t)，z = t，其中s∈[0,8]，t∈[0,5π]。这个参数方程看起来像是一个指数衰减的螺旋线，随着s的增加，x和y的幅度会按e^{-s}衰减，而z随着t线性增加。因此，当s从0到8时，螺旋的半径会迅速减小，形成一个类似于锥形的螺旋结构，而z轴则随着t的增加而上升，形成类似弹簧的形状，但半径逐渐缩小。因此，整个曲面应该是一个沿着z轴延伸的螺旋带，随着高度的增加，螺旋的半径越来越小，最终趋向于零。可能图像显示为螺旋线随着高度增加而逐渐收紧，形成类似锥形螺旋的曲面。
---

## 五、实验总结与讨论

- 通过本实验你掌握了哪些绘图技巧？使用SymPy的plot函数绘制显式函数，处理不连续点；使用plot_implicit绘制隐式方程，并注意避免数学错误（如除以零）；使用plot3d_parametric_surface绘制三维参数曲面，设置参数范围和标签。
- 实验中你遇到了哪些问题？如何解决？问题3中需要正确设置s和t的范围以确保曲面完整显示。通过合理选择参数范围（如s∈[0,8]和t∈[0,5π]），成功绘制螺旋曲面。问题1中cos(tan(πx))在x=0.5附近存在不连续点。SymPy的plot函数自动处理了这些点，但图像仍会出现断裂，需通过调整绘图范围或接受图像的局限性。
- 你对SymPy的绘图功能有什么建议或意见？隐函数绘图时处理除零错误的更友好方式，或者更灵活的区间设置（如允许不连续的区间）；或者三维绘图的交互性改进，或者更多的自定义选项。

---

## 六、参考文献

- SymPy官方文档：https://docs.sympy.org/latest/modules/plotting.html

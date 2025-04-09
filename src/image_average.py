import numpy as np
import scipy.ndimage as sim
import matplotlib.pyplot as plt


def create_small_filter():
    """
    创建3×3平均滤波器

    返回:
        numpy.ndarray: 3×3的滤波器矩阵，每个元素值为1/9
    """
    # 创建3x3全1矩阵并归一化
    return np.ones((3, 3)) / 9


def create_large_filter():
    """
    创建15×15平均滤波器

    返回:
        numpy.ndarray: 15×15的滤波器矩阵，每个元素值为1/225
    """
    # 创建15x15全1矩阵并归一化
    return np.ones((15, 15)) / 225


def process_image(input_file):
    """
    处理图像并显示原始图像和滤波后的结果

    参数:
        input_file (str): 输入图像文件路径
    """
    # 1. 读取图像
    img = plt.imread(input_file)

    # 如果图像是彩色(RGB)，转换为灰度（根据实际情况调整）
    if img.ndim == 3:
        img = np.mean(img, axis=2)

    # 2. 创建滤波器
    small_filter = create_small_filter()
    large_filter = create_large_filter()

    # 3. 应用卷积
    small_result = sim.convolve(img, small_filter, mode='nearest')
    large_result = sim.convolve(img, large_filter, mode='nearest')

    # 4. 显示结果
    plt.figure(figsize=(15, 5))

    # 原始图像
    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    # 3×3滤波结果
    plt.subplot(1, 3, 2)
    plt.imshow(small_result, cmap='gray')
    plt.title('3×3 Filter Result')
    plt.axis('off')

    # 15×15滤波结果
    plt.subplot(1, 3, 3)
    plt.imshow(large_result, cmap='gray')
    plt.title('15×15 Filter Result')
    plt.axis('off')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    from scipy.signal import fftconvolve
    large_result = fftconvolve(img, large_filter, mode='same')
    process_image('data/bwCat.tif')

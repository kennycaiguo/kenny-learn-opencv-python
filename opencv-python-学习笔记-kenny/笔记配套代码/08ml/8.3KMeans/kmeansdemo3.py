# -*- encoding:utf-8 -*-
# @日期和时间：2024/7/14 16:37
# @Author: Kenny cai
# @File name:kmeansdemo3.py.py
# @dev tool:PyCharm

# https://blog.csdn.net/first_bug/article/details/123514692
import numpy as np
import cv2
import matplotlib.pyplot as plt

# 读取待处理图像
img = cv2.imread('./hand2.jpg')
# 使用reshape将一个像素点的RGB值作为一个单元处理
data = img.reshape((-1, 3))  # n行 3列
# 转换为kmeans可以处理的类型
data = np.float32(data)
# 调用kmeans模块
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
ret, label, center = cv2.kmeans(data, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# 转换为uint8数据类型，将每个像素点都赋值为当前分类的中心点像素值
# 将center的值转换为uint8
center = np.uint8(center)
# 使用center内的值替换原像素点的值
res1 = center[label.flatten()]  # 根据索引来取值，最后结果的大小同索引的大小
# 使用reshape调整替换后的图像
res2 = res1.reshape((img.shape))
# 显示处理结果
plt.subplot(121)
plt.imshow(img[:, :, ::-1])
plt.axis('off')
plt.subplot(122)
plt.imshow(res2[:, :, ::-1])
plt.axis('off')
plt.show()

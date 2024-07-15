# -*- encoding:utf-8 -*-
# @日期和时间：2024/7/14 17:10
# @Author: Kenny cai
# @File name:kmeansdemo4.py.py
# @dev tool:PyCharm

"""
 https://juejin.cn/post/7023696890843627557
 单特征聚类、多特征聚类、颜色量化
 1.只有一个特征的数据（T恤问题，只根据身高）
"""
# OpenCV实现K-Means Cluster K均值聚类
# 输入参数
# - samples: np.float32 数据类型，每个特征放在一个列中。
# - nclusters(K) : 最后需要的簇数
# - creteria: 迭代终止标准。当满足此条件时，算法迭代停止。实际上，它应该是一个包含 3 个参数的元组。它们是（类型、max_iter、epsilon）：
#  a - 终止条件的类型：它有 3 个标志，如下所示：cv2.TERM_CRITERIA_EPS - 如果达到指定的准确度 epsilon，则停止算法迭代。
#                                             cv2.TERM_CRITERIA_MAX_ITER - 在指定的迭代次数 max_iter 后停止算法。
#                                             cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER - 当满足上述任何条件时停止迭代。
# b - 最大迭代次数 - 指定最大迭代次数的整数。
# c - 精度 - 要求的准确性
# - attempts ：标记以指定使用不同的初始标签执行算法的次数。该算法返回产生最佳紧凑性的标签。这种紧凑性作为输出返回。
# - flags ：此标志用于指定如何采用初始中心。通常为此使用两个标志：cv2.KMEANS_PP_CENTERS 和 cv2.KMEANS_RANDOM_CENTERS。

#
# 输出参数
#
# - compactness: 紧凑度，指每个点到其相应中心的距离平方和
# - labels: 标签数组，其中每个元素都标记为“0”、“1”.....
# - centers: 聚簇中心的数组

# 1. 只有一个特征的数据（T恤问题，只根据身高）
import numpy as np
import cv2
from matplotlib import pyplot as plt

x = np.random.randint(25, 100, 25)
y = np.random.randint(175, 255, 25)
z = np.hstack((x, y))
z = z.reshape((50, 1))
z = np.float32(z)
plt.hist(z, 256, [0, 256]), plt.show()

# 每当运行 10 次算法迭代或达到 epsilon = 1.0 的准确度时，停止算法并返回
# 定义终止准则 criteria = ( type, max_iter = 10 , epsilon = 1.0 )
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# 设置标志（只是为了避免代码中的换行符）
flags = cv2.KMEANS_RANDOM_CENTERS

# 应用K均值聚类算法
compactness, labels, centers = cv2.kmeans(z, 2, None, criteria, 10, flags)

A = z[labels == 0]
B = z[labels == 1]

# 以红色绘制 A，以蓝色绘制 B，以黄色绘制它们的质心。
plt.hist(A, 256, [0, 256], color='r')
plt.hist(B, 256, [0, 256], color='b')
plt.hist(centers, 32, [0, 256], color='y')
plt.title("one feature res")
plt.show()

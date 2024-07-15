# -*- encoding:utf-8 -*-
# @日期和时间：2024/7/14 17:10
# @Author: Kenny cai
# @File name:kmeansdemo4.py.py
# @dev tool:PyCharm

"""
 https://juejin.cn/post/7023696890843627557
 单特征聚类、多特征聚类、颜色量化
 2. 具有多重数据的特征（T恤问题，根据身高、体重）
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

X = np.random.randint(25, 50, (25, 2))  # 身高
Y = np.random.randint(60, 85, (25, 2))  # 体重
Z = np.vstack((X, Y))

# 转换为 np.float32
Z = np.float32(Z)

# 定义终止准则以及应用KMeans聚类
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, label, center = cv2.kmeans(Z, 2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# 分离数据，并拉平flatten
A = Z[label.ravel() == 0]
B = Z[label.ravel() == 1]

# 绘制数据
plt.scatter(A[:, 0], A[:, 1])
plt.scatter(B[:, 0], B[:, 1], c='r')
plt.scatter(center[:, 0], center[:, 1], s=80, c='y', marker='s')
plt.xlabel('Height'), plt.ylabel('Weight')
plt.title("two features res")
plt.show()
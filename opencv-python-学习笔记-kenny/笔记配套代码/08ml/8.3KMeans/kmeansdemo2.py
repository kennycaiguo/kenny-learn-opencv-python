# -*- encoding:utf-8 -*-
# @日期和时间：2024/7/14 16:32
# @Author: Kenny cai
# @File name:kmeansdemo2.py.py
# @dev tool:PyCharm

# https://blog.csdn.net/first_bug/article/details/123514692
import numpy as np
import cv2
from matplotlib import pyplot as plt

# 随机生成两组数值
# 长和宽都在[0,20]内
m1 = np.random.randint(0, 20, (30, 2))
# 长和宽的大小都在[40,60]
m2 = np.random.randint(40, 60, (30, 2))
# 组合数据
m = np.vstack((m1, m2))
# 转换为float32类型
m = np.float32(m)
# 调用kmeans模块
# 设置参数criteria值
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# 调用kmeans函数
ret, label, center = cv2.kmeans(m, 2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

''' 
#打印返回值 
print(ret) 
print(label) 
print(center) 
'''
# 根据kmeans的处理结果，将数据分类，两大类
res1 = m[label.ravel() == 0]
res2 = m[label.ravel() == 1]
# 绘制分类结果数据及中心点
plt.scatter(res1[:, 0], res1[:, 1], c='g', marker='s')
plt.scatter(res2[:, 0], res2[:, 1], c='r', marker='o')
plt.scatter(center[0, 0], center[0, 1], s=200, c='b', marker='o')
plt.scatter(center[1, 0], center[1, 1], s=200, c='b', marker='s')
plt.xlabel('Height'), plt.ylabel('Width')
plt.show()


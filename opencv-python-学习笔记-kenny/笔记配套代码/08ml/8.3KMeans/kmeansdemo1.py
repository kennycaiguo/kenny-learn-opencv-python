# -*- encoding:utf-8 -*-
# @日期和时间：2024/7/14 16:30
# @Author: Kenny cai
# @File name:kmeansdemo1.py
# @dev tool:PyCharm

#https://blog.csdn.net/first_bug/article/details/123514692
import numpy as np
import cv2
from matplotlib import pyplot as plt

# 随机生成两组数组
# 生成60个值在[0,50]内的数据
num1 = np.random.randint(0, 50, 60)
# 生成60个值在[200,250]内的数据
num2 = np.random.randint(200, 250, 60)
# 组合数据为num
num = np.hstack((num1, num2))
# 使用reshape函数将其转换为(120,1)
num = num.reshape((120, 1))  # 每个数据为1列
# 转换为float32类型
num = np.float32(num)
# 调用kmeans模块
# 设置参数criteria的值
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# 设置参数flags的值
flags = cv2.KMEANS_RANDOM_CENTERS
# 调用函数kmeans
retval, bestLabels, centers = cv2.kmeans(num, 2, None, criteria, 10, flags)

# 打印返回值
print(retval)
print(bestLabels)
print(centers)

# 获取分类结果
n1 = num[bestLabels == 0]
n2 = num[bestLabels == 1]

# 绘制分类结果
# 绘制原始数据
plt.plot(np.ones(len(n1)), n1, 'ro')
plt.plot(np.ones(len(n2)), n2, 'bo')
# 绘制中心点
# plt.plot([1],centers[0],'rx')
# plt.plot([1],centers[1],'bx')
plt.show()

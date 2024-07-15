# -*- encoding:utf-8 -*-
# @日期和时间：2024/7/14 17:10
# @Author: Kenny cai
# @File name:kmeansdemo4.py.py
# @dev tool:PyCharm

"""
https://blog.csdn.net/cyj972628089/article/details/122033850
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt
# 随机生成两组数组
# 生成60 个值在[0,50]内的xiaoMI 直径数据
xiaoMI = np.random.randint(0,50,60)
# 生成60 个值在[200,250]内的daMI 直径数据
daMI = np.random.randint(200,250,60)
# 将xiaoMI 和daMI 组合为MI
MI = np.hstack((xiaoMI,daMI))
# 使用reshape 函数将其转换为(120,1)
MI = MI.reshape((120,1))
# 将MI 转换为float32 类型
MI = np.float32(MI)
# 调用kmeans 模块
# 设置参数criteria 的值
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# 设置参数flags 的值
flags = cv2.KMEANS_RANDOM_CENTERS
# 调用函数kmeans
retval,bestLabels,centers = cv2.kmeans(MI,2,None,criteria,10,flags)
'''
# 打印返回值
print(retval)
print(bestLabels)
print(centers)
'''
# 获取分类结果
XM = MI[bestLabels==0]
DM = MI[bestLabels==1]
# 绘制分类结果
# 绘制原始数据
plt.plot(XM,'ro')
plt.plot(DM,'bo')
# 绘制中心点
plt.plot(centers[0],'rx')
plt.plot(centers[1],'bx')
plt.show()

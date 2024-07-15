# -*- encoding:utf-8 -*-
# @日期和时间：2024/7/14 16:12
# @Author: Kenny cai
# @File name:svm-demo3-nolinear.py
# @dev tool:PyCharm
"""
非线性向量机实例
"""

from __future__ import print_function

import random as rng

import cv2 as cv
import numpy as np

NTRAINING_SAMPLES = 100  # Number of training samples per class
FRAC_LINEAR_SEP = 0.9  # Fraction of samples which compose the linear separable part

# 可视化窗口大小
WIDTH = 512
HEIGHT = 512
I = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

# 随机生成训练数据
trainData = np.empty((2 * NTRAINING_SAMPLES, 2), dtype=np.float32)
labels = np.empty((2 * NTRAINING_SAMPLES, 1), dtype=np.int32)

rng.seed(100)  # 随机生成分类标签

# 为训练数据设置线性分离区
# Set up the linearly separable part of the training data
nLinearSamples = int(FRAC_LINEAR_SEP * NTRAINING_SAMPLES)

# 为分类1生成随机点
trainClass = trainData[0:nLinearSamples, :]
# x在[0,0.4]
c = trainClass[:, 0:1]
c[:] = np.random.uniform(0.0, 0.4 * WIDTH, c.shape)
# y在[0, 1)
c = trainClass[:, 1:2]
c[:] = np.random.uniform(0.0, HEIGHT, c.shape)

# 为分类2生成随机点
trainClass = trainData[2 * NTRAINING_SAMPLES - nLinearSamples:2 * NTRAINING_SAMPLES, :]
# x在 [0.6, 1]
c = trainClass[:, 0:1]
c[:] = np.random.uniform(0.6 * WIDTH, WIDTH, c.shape)
# y在 [0, 1)
c = trainClass[:, 1:2]
c[:] = np.random.uniform(0.0, HEIGHT, c.shape)

# 为测试数据集的分类1，2分别生成随机点
trainClass = trainData[nLinearSamples:2 * NTRAINING_SAMPLES - nLinearSamples, :]
# x在[0.4,0.6]
c = trainClass[:, 0:1]
c[:] = np.random.uniform(0.4 * WIDTH, 0.6 * WIDTH, c.shape)
# y在[0,1]
c = trainClass[:, 1:2]
c[:] = np.random.uniform(0.0, HEIGHT, c.shape)

# 设置分类标签1及2
labels[0:NTRAINING_SAMPLES, :] = 1  # 分类1
labels[NTRAINING_SAMPLES:2 * NTRAINING_SAMPLES, :] = 2  # 分类2

# 开始训练，首先设置支持向量机SVM参数
print('Starting training process')
# 初始化
svm = cv.ml.SVM_create()
svm.setType(cv.ml.SVM_C_SVC)
svm.setC(0.1)
svm.setKernel(cv.ml.SVM_LINEAR)
svm.setTermCriteria((cv.TERM_CRITERIA_MAX_ITER, int(1e7), 1e-6))

# 训练SVM
svm.train(trainData, cv.ml.ROW_SAMPLE, labels)

# 结束训练
print('Finished training process')

# 展示决策区域（绘制蓝色，绿色） 分类1为绿色，分类2为蓝色
green = (0, 100, 0)
blue = (100, 0, 0)
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        sampleMat = np.matrix([[j, i]], dtype=np.float32)
        response = svm.predict(sampleMat)[1]
        if response == 1:
            I[i, j] = green
        elif response == 2:
            I[i, j] = blue

# 展示测试数据
thick = -1

# 分类1 绿色
for i in range(NTRAINING_SAMPLES):
    px = trainData[i, 0]
    py = trainData[i, 1]
    cv.circle(I, (px, py), 3, (0, 255, 0), thick)

# 分类2 蓝色
for i in range(NTRAINING_SAMPLES, 2 * NTRAINING_SAMPLES):
    px = trainData[i, 0]
    py = trainData[i, 1]
    cv.circle(I, (px, py), 3, (255, 0, 0), thick)

# 展示支持向量
thick = 2
sv = svm.getUncompressedSupportVectors()

for i in range(sv.shape[0]):
    cv.circle(I, (sv[i, 0], sv[i, 1]), 6, (128, 128, 128), thick)

cv.imwrite('non_linear_svms_result.png', I)  # 保存图片
cv.imshow('SVM for Non-Linear Training Data', I)  # 展示图片结果
cv.waitKey()

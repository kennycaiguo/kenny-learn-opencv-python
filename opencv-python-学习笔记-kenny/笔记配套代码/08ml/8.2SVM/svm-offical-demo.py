# -*- encoding:utf-8 -*-
# @日期和时间：2024/7/14 15:42
# @Author: Kenny cai
# @File name:svm-offical-demo.py
# @dev tool:PyCharm

from __future__ import print_function
import cv2 as cv
import numpy as np
import random as rng
import time
from matplotlib import pyplot as plt

NTRAINING_SAMPLES = 100 # 每个类别的训练样本数
FRAC_LINEAR_SEP = 0.9   # 线性可分的样本比例

# 准备用于数据可视化
WIDTH = 512
HEIGHT = 512
I = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

# 设置训练样本
trainData = np.empty((2*NTRAINING_SAMPLES, 2), dtype=np.float32)
labels = np.empty((2*NTRAINING_SAMPLES, 1), dtype=np.int32)

rng.seed(100) # Random value generation class

# 线性可分的训练样本数量
nLinearSamples = int(FRAC_LINEAR_SEP * NTRAINING_SAMPLES)

## [setup1]
# 生成class 1的随机点，随机点的x坐标在[0, 0.4)，y坐标在 [0, 1)
trainClass = trainData[0:nLinearSamples,:]
# The x coordinate of the points is in [0, 0.4)
c = trainClass[:,0:1]
c[:] = np.random.uniform(0.0, 0.4 * WIDTH, c.shape)
# The y coordinate of the points is in [0, 1)
c = trainClass[:,1:2]
c[:] = np.random.uniform(0.0, HEIGHT, c.shape)

# 生成class 2的随机点，随机点的x坐标在[0.6, 1]，y坐标在 [0, 1)
trainClass = trainData[2*NTRAINING_SAMPLES-nLinearSamples:2*NTRAINING_SAMPLES,:]
# The x coordinate of the points is in [0.6, 1]
c = trainClass[:,0:1]
c[:] = np.random.uniform(0.6*WIDTH, WIDTH, c.shape)
# The y coordinate of the points is in [0, 1)
c = trainClass[:,1:2]
c[:] = np.random.uniform(0.0, HEIGHT, c.shape)

# 设置线性不可分的训练样本
# Generate random points for the classes 1 and 2
trainClass = trainData[nLinearSamples:2*NTRAINING_SAMPLES-nLinearSamples,:]
# x坐标在 [0.4, 0.6)，y坐标在[0, 1)
c = trainClass[:,0:1]
c[:] = np.random.uniform(0.4*WIDTH, 0.6*WIDTH, c.shape)
c = trainClass[:,1:2]
c[:] = np.random.uniform(0.0, HEIGHT, c.shape)

# 设置两个类别的label
labels[0:NTRAINING_SAMPLES,:] = 1                   # Class 1
labels[NTRAINING_SAMPLES:2*NTRAINING_SAMPLES,:] = 2 # Class 2

# 设置SVM参数，初始化模型：

print('Starting training process')
svm = cv.ml.SVM_create()
svm.setType(cv.ml.SVM_C_SVC)
svm.setC(0.1)
svm.setKernel(cv.ml.SVM_LINEAR)
svm.setTermCriteria((cv.TERM_CRITERIA_MAX_ITER, int(1e7), 1e-6))
# 训练SVM：

## 训练
svm.train(trainData, cv.ml.ROW_SAMPLE, labels)
print('Finished training process')

## 显示决策区域
green = (0,100,0)
blue = (100,0,0)
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        sampleMat = np.matrix([[j,i]], dtype=np.float32)
        response = svm.predict(sampleMat)[1]

        if response == 1:
            I[i,j] = green
        elif response == 2:
            I[i,j] = blue

# 对训练集中两个类别的样本进行可视化：

## 用两种颜色圆圈表示class 1和class 2的训练数据
thick = -1
# Class 1
for i in range(NTRAINING_SAMPLES):
    px = trainData[i,0]
    py = trainData[i,1]
    cv.circle(I, (px, py), 3, (0, 255, 0), thick)

# Class 2
for i in range(NTRAINING_SAMPLES, 2*NTRAINING_SAMPLES):
    px = trainData[i,0]
    py = trainData[i,1]
    cv.circle(I, (px, py), 3, (255, 0, 0), thick)

# 显示支持向量（
## [show_vectors]
thick = 2
sv = svm.getUncompressedSupportVectors()

for i in range(sv.shape[0]):
    cv.circle(I, (sv[i,0], sv[i,1]), 6, (128, 128, 128), thick)
## [show_vectors]

#cv.imwrite('result.png', I)                      # save the Image
#cv.imshow('SVM for Non-Linear Training Data', I) # show it to the user
plt.imshow(I)
plt.show()

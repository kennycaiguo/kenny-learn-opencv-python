# -*- encoding:utf-8 -*-
# @日期和时间：2024/7/14 15:53
# @Author: Kenny cai
# @File name:svmdemo2-linear.py
# @dev tool:PyCharm

import cv2
import numpy as np

SZ = 20
bin_n = 16  # Number of bins

svm_params = dict(kernel_type=cv2.ml.SVM_LINEAR,
                  svm_type=cv2.ml.SVM_C_SVC,
                  C=2.67, gamma=5.383)

affine_flags = cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR


# 左图像是原始图像，右图像是倾斜图像。
def deskew(img):
    m = cv2.moments(img)
    if abs(m['mu02']) < 1e-2:
        return img.copy()
    skew = m['mu11'] / m['mu02']
    M = np.float32([[1, skew, -0.5 * SZ * skew], [0, 1, 0]])
    img = cv2.warpAffine(img, M, (SZ, SZ), flags=affine_flags)
    return img


# （HOG Histogram of Oriented Gradients）方向梯度直方图
def hog(img):
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
    mag, ang = cv2.cartToPolar(gx, gy)

    # 量化 (0...16)的binvalues
    bins = np.int32(bin_n * ang / (2 * np.pi))

    # 分成四个子块
    bin_cells = bins[:10, :10], bins[10:, :10], bins[:10, 10:], bins[10:, 10:]
    mag_cells = mag[:10, :10], mag[10:, :10], mag[:10, 10:], mag[10:, 10:]
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)
    return hist


img = cv2.imread('./digits.png', 0)
print(img.shape)  # (1000,2000)

cells = [np.hsplit(row, 100) for row in np.vsplit(img, 50)]
print(len(cells))  # 50*100

# 一半数据用于训练，一半用于测试(前50列，后50列）
train_cells = [i[:50] for i in cells]
test_cells = [i[50:] for i in cells]

# cv2.imshow("img", train_cells[0][0])
# cv2.imshow("deskew", deskew(train_cells[0][0]))
# cv2.waitKey(0)

# 训练数据
deskewed = [list(map(deskew, row)) for row in train_cells]
hogdata = [list(map(hog, row)) for row in deskewed]

trainData = np.float32(hogdata).reshape(-1, 64)
responses = np.repeat(np.arange(10), 250)[:, np.newaxis]
print('trainData: ', type(trainData), len(trainData))
print('responses: ', type(responses), responses.shape, len(responses))

print(responses[0])

svm = cv2.ml.SVM_create()
svm.setGamma(svm_params['gamma'])
svm.setC(svm_params['C'])
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setType(cv2.ml.SVM_C_SVC)
svm.train(trainData, cv2.ml.ROW_SAMPLE, responses)

# 把训练的数据及模型保存下来
svm.save('./svm_data.dat')

# 测试数据
deskewed = [list(map(deskew, row)) for row in test_cells]
hogdata = [list(map(hog, row)) for row in deskewed]
testData = np.float32(hogdata).reshape(-1, bin_n * 4)
result = svm.predict(testData)[1]

print('result: ', type(result))
print('responses: ', type(responses))

# 检查准确度
mask = result == responses
correct = np.count_nonzero(mask)
print('correct: ', correct)

# SVM得到93.8%的准确度，比KNN的91.76%要高一些
print(correct * 100.0 / len(list(result)))



# -*- encoding:utf-8 -*-
# @日期和时间：2024/7/14 17:10
# @Author: Kenny cai
# @File name:kmeansdemo4.py.py
# @dev tool:PyCharm

"""
 https://juejin.cn/post/7023696890843627557
 单特征聚类、多特征聚类、颜色量化
 3. 颜色量化
# 颜色量化是减少图像中颜色数量的过程。这样做的原因之一是减少内存。有时某些设备可能有限制，以至于它只能产生有限数量的颜色。
# 在这些情况下，也会执行颜色量化。这里我们使用 k-means 聚类进行颜色量化。有3个特征，例如 R、G、B。需要将图像重塑为 Mx3 大小的数组（M 是图像中的像素数）。
# 在聚类之后将质心值（也是 R、G、B）应用于所有像素，这样生成的图像将具有指定数量的颜色，最后需要将其重塑回原始图像的形状。
"""
import numpy as np
import cv2

img = cv2.imread('./ml.png')
Z = img.reshape((-1, 3))

# 转换 np.float32
Z = np.float32(Z)

# 定义终止准则以及应用KMeans聚类
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 15
ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# 转换回uint8, 制作原始图像
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow("origin",img)
cv2.imshow('res2', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
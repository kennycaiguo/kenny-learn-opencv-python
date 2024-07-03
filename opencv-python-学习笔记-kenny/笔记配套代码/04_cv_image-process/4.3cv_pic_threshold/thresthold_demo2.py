import cv2
import numpy as np
from matplotlib import  pyplot as plt
"""
自适应阈值处理:cv2.adaptiveThreshold,注意这个方法只有一个返回值
在上面，我们使用全局值作为阈值，但在图像在不同区域具有不同照明条件的所有条件下可能并不好。在那种情况下，我们进行自适应阈值处理，算法计算图像的小区域的阈值，所以我们对同一幅图像的不同区域给出不同的阈值，这给我们在不同光照下的图像提供了更好的结果。

这种阈值处理方法有三个指定输入参数和一个输出参数。

Adaptive Method - 自适应方法，决定如何计算阈值。

cv.ADAPTIVE_THRESH_MEAN_C：阈值是邻域的平均值。
cv.ADAPTIVE_THRESH_GAUSSIAN_C：阈值是邻域值的加权和，其中权重是高斯窗口。
Block Size - 邻域大小，它决定了阈值区域的大小。

C - 它只是从计算的平均值或加权平均值中减去的常数。
"""
img = cv2.imread('../mydata/sudoku.png', 0)  # 填写图片名称
img = cv2.medianBlur(img,5)
ret,threshold1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
threshold2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
threshold3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# 使用cv2.ADAPTIVE_THRESH_GAUSSIAN_C处理的效果很好

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [
    img,
    threshold1,
    threshold2,
    threshold3,
]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

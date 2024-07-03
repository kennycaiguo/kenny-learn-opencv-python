import cv2
import numpy as np
from matplotlib import pyplot as plt
"""
Sobel算子和拉普拉斯算子效果对比
Sobel算子有x方向和y方向的处理
"""

# img = cv2.imread('../mydata/sudoku.png',0)  # 需要转化为灰度图片
img = cv2.imread('../mydata/ml.png',0)  # 需要转化为灰度图片
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobel_x = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=9)
sobel_y = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=9)
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray'),plt.title("Original"),plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray'),plt.title("Laplacian"),plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobel_x,cmap = 'gray'),plt.title("Sobel axis x"),plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobel_y,cmap = 'gray'),plt.title("Sobel axis y"),plt.xticks([]), plt.yticks([])
plt.show()

# cv2.imshow("pic", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
from matplotlib import  pyplot as plt
"""
简单阈值处理
这种阈值处理的方法是简单易懂的。如果像素值大于阈值，则为其分配一个值（可以是白色），否则为其分配另一个值（可以是黑色）。
使用的函数是cv.threshold。函数第一个参数是源图像，它应该是灰度图像。第二个参数是用于对像素值进行分类的阈值。
第三个参数是maxVal，它表示如果像素值大于（有时小于）阈值则要给出的值。OpenCV提供不同类型的阈值，由函数的第四个参数决定。
不同的类型有：

cv.THRESH_BINARY
cv.THRESH_BINARY_INV
cv.THRESH_TRUNC
cv.THRESH_TOZERO
cv.THRESH_TOZERO_INV
文档清楚地解释了每种类型的含义。

函数将获得两个输出。第一个是retavl，将在后面解释它的作用。第二个输出是我们的阈值图像。
"""
img = cv2.imread('../mydata/gradient.png', 0)  # 填写图片名称
ret,threshold1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,threshold2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,threshold3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,threshold4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,threshold5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [
    img,
    threshold1,
    threshold2,
    threshold3,
    threshold4,
    threshold5,
]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
from matplotlib import  pyplot as plt
"""
 在第一节中，我只告诉你另一个参数是retVal，但没告诉你它的作用。其实，它是用来进行Otsu's二值化。

在全局阈值处理中，我们使用任意值作为阈值，那么，我们如何知道我们选择的值是好还是不好？答案是，试错法。
但如果是双峰图像（简单来说，双峰图像是直方图有两个峰值的图像）我们可以将这些峰值中间的值近似作为阈值，这就是Otsu二值化的作用。简单来说，
它会根据双峰图像的图像直方图自动计算阈值。（对于非双峰图像，二值化不准确。）

为此，使用了我们的cv.threshold()函数，但是需要多传递一个参数cv.THRESH_OTSU。这时要吧阈值设为零。然后算法找到最佳阈值并返回第二个输出retVal。
如果未使用Otsu二值化，则retVal与你设定的阈值相同。

请查看以下示例。输入图像是嘈杂的图像。在第一种情况下，我将全局阈值应用为值127。在第二种情况下，我直接应用了Otsu的二值化。在第三种情况下，我使用5x5
高斯卷积核过滤图像以消除噪声，然后应用Otsu阈值处理。来看看噪声过滤如何改善结果。
"""
img = cv2.imread('../mydata/noisy2.png', 0)  # 填写图片名称
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(img,(5,5),0) #高斯模糊处理
ret,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# 使用cv2.ADAPTIVE_THRESH_GAUSSIAN_C处理的效果很好

# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]

titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

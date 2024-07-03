import cv2
import numpy as np

"""
有时您需要分别处理图像的B、G、R通道。在这种情况下，需要将BGR图像分割为单个通道。或者在其他情况下，可能需要将这些单独的通道合并到BGR图像。你可以通过以下方式完成：

>>> b,g,r = cv.split(img)
>>> img = cv.merge((b,g,r))
或者：

>>> b = img[:,:,0]
假设你要将所有红色像素设置为零，则无需先拆分通道。使用Numpy索引更快：

>>> img[:,:,2] = 0
注意：cv.split()是一项代价高昂的操作（就消耗时间而言）。所以只有在你需要时才这样做。否则使用Numpy索引。
"""

img = cv2.imread('messi2.png')  # 填写图片名称
b,g,r = cv2.split(img)
cv2.imshow("pic",np.vstack((b,g,r)))
img2 = cv2.merge((b,g,r,r//2))
# img2 = cv2.merge((r,g,b))
cv2.imshow("pic2",img2)
# img[:,:,2] = 0
# img[:,:,1] = 0
img[:,:,0] = 0
cv2.imshow("pic3",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
"""
无论图片平移，旋转都可以使用cv2.warpAffine(src,M,(w,h))来做
需要平移的话，输入平移矩阵[[1,0,x],[0,1,y]]
需要旋转的的话，使用cv2.getRotationMatrix2D((x,y),角度,缩放比例)获取旋转矩阵M，然后调用cv2.warpAffine(src,M,(w,h))
"""

img = cv2.imread('../mydata/messi5.jpg')  # 填写图片名称
h,w = img.shape[:2]
# 平移矩阵[[1,0,x],[0,1,y]]
matrix = cv2.getRotationMatrix2D((w/2,h/2),90,1)
dst = cv2.warpAffine(img,matrix,(w,h))

cv2.imshow("rotate", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

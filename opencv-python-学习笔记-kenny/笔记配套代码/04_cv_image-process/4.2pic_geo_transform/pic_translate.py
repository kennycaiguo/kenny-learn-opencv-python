import cv2
import numpy as np

img = cv2.imread('../mydata/messi5.jpg')  # 填写图片名称
h,w = img.shape[:2]
# 平移矩阵[[1,0,x],[0,1,y]
matrix = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,matrix,(w,h))

cv2.imshow("pic", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

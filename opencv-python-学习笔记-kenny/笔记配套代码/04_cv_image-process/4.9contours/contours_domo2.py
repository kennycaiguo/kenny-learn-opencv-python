import cv2
import numpy as np

img = cv2.imread('../mydata/pic3.png')  # 填写图片名称
img2 = img.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,th = cv2.threshold(gray,127,255,0) # 进行轮廓查找之前需要先进行二值化或者Canny边缘检测
th = cv2.Canny(img,127,255)
ret,contours,hierarchy = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # 3.6版本
# 查找到的contour不能直接显示，需要用drawContours绘制处来
cv2.drawContours(img2,contours,-1,(0,255,125),3)
cv2.imshow("org", img)
cv2.imshow("contours", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

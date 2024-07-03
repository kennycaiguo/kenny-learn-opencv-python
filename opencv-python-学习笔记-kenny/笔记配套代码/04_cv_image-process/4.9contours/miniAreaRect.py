import cv2
import numpy as np

img = cv2.imread('../mydata/shape.png')  # 填写图片名称
cv2.imshow("original", img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,th = cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
_,contours,hierary = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img1 = np.zeros(img.shape,np.uint8)+255
cv2.drawContours(img1,contours,-1,(0,0,255),3)
cv2.imshow('Contours',img1)
# 获取旋转矩形数据，并且做适当转换处理
ret = cv2.minAreaRect(contours[0])
rect = cv2.boxPoints(ret)
rect = np.int0(rect)
img2 = img.copy()
cv2.drawContours(img2,[rect],-1,(255,255,0),3)
cv2.imshow('miniAreaRect',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

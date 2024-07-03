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
# 计算最小外接三角形数据
ret,triangle = cv2.minEnclosingTriangle(contours[0])
triangle = np.int0(triangle)
img2 = img.copy()
# 绘制三角形，使用polyLine方法
cv2.polylines(img2,[triangle],True,(0,255,255),2)
cv2.imshow('Enclosed Triangle',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

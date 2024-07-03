import cv2
import numpy as np
"""
solidity，密实比或者叫做稳固性，计算方法轮廓面积/凸包面积
"""

img = cv2.imread('../../mydata/tubao.jpeg')  # 填写图片名称
cv2.imshow("original", img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 二值化，取阈值为235
ret,th = cv2.threshold(gray,235,255,cv2.THRESH_BINARY)
# 查找轮廓
_,contours,hierary = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
# 计算轮廓面积
area = cv2.contourArea(cnt)
# 计算凸包的面积
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area
print("Solidity",solidity)
img2 = img.copy()
length = len(hull)
for i in range(len(hull)):
    cv2.line(img2,tuple(hull[i][0]),tuple(hull[(i+1)%length][0]),(0,0,255),2)

cv2.imshow("Result", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

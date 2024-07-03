import cv2
import numpy as np

img = cv2.imread('../mydata/hand2.jpg')  # 填写图片名称
# 转换位灰度图
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 二值化
ret,th = cv2.threshold(gray,70,255,cv2.THRESH_BINARY)
_,contours,hierary = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img2 = img.copy()
cv2.drawContours(img2,contours,-1,(255,0,0),2)
cv2.imshow('contours',img2)
# cnt = contours[0]
for cnt in contours:
    hull = cv2.convexHull(cnt)
    length = len(hull)
    # 绘制
    for i in range(len(hull)):
        cv2.line(img,tuple(hull[i][0]),tuple(hull[(i+1)%length][0]),(0,255,0),3)
        cv2.imshow("hull", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

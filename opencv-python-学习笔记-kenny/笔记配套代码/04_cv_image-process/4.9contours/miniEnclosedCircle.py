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
# 计算最新外接圆的圆心和半径，然后绘制
(x,y),radius = cv2.minEnclosingCircle(contours[0])
center = (int(x),int(y))
radius = int(radius)
img2 = img.copy()
cv2.circle(img2,center,radius,(0,255,0),2)
cv2.imshow('Enclosed circle',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

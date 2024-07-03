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
# 计算拟合直线数据
[vx,vy,x,y] = cv2.fitLine(contours[0],cv2.DIST_L1,0,0.01,0.01)
img2 = img.copy()
rows, cols = img.shape[:2]
# 绘制拟合直线，还是有点难度的，慢慢体会
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
cv2.line(img2, (0, lefty), (cols-1, righty), (255,0,0), 2)
cv2.imshow('fit Line',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

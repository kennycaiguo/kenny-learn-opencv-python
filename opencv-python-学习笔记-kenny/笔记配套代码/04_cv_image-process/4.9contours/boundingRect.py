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
b_rect = cv2.boundingRect(contours[0])
pt1 = (b_rect[0],b_rect[1])
pt2 = (b_rect[0]+b_rect[2],b_rect[1]+b_rect[3])
img2 = img.copy()
cv2.rectangle(img2,pt1,pt2,(0,255,0),3)
cv2.imshow('boundingRect',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

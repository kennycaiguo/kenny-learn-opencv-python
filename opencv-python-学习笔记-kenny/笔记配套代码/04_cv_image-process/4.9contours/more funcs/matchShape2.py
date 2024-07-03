import cv2
import numpy as np
img = cv2.imread('../../mydata/shapes.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,th = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_,contours,_ = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # 第一个是l第二个是小星形，第三个的大星形
cnt0,cnt1,cnt2 = contours[0],contours[1],contours[2]

cv2.drawContours(img,[cnt0],-1,(0,0,255),3)
cv2.drawContours(img,[cnt1],-1,(0,0,255),3)
cv2.drawContours(img,[cnt2],-1,(0,0,255),3)
print("a=>a",cv2.matchShapes(cnt0,cnt0,1,0.0)) # a是两个矩形组合体，b是小星形，c是大星形
print("a=>b",cv2.matchShapes(cnt0,cnt1,1,0.0))
print("a=>c",cv2.matchShapes(cnt0,cnt2,1,0.0))
print("b=>c",cv2.matchShapes(cnt1,cnt2,1,0.0))

cv2.imshow("contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

img = cv2.imread('../../mydata/sijiaoxing.png')  # 填写图片名称
cv2.imshow("pic", img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,th = cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
_,contours,hierarchy = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
hull = cv2.convexHull(cnt,returnPoints=False)  # 注意，如果需要获取凸缺陷点，需要returnPoints = False
defects = cv2.convexityDefects(cnt,hull)
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,(0,255,0),2)
    cv2.circle(img,far,5,(255,0,0),-1)
cv2.imshow('res',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

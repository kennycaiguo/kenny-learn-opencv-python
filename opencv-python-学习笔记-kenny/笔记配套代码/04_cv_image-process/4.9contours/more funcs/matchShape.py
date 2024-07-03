import cv2
import numpy as np

img = cv2.imread('../../mydata/sm_star.png')  # 填写图片名称
img2 = cv2.imread('../../mydata/star2.jpg')
gray1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

ret,th1 = cv2.threshold(gray1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret,th2 = cv2.threshold(gray2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_,cnt1,hier1 = cv2.findContours(th1,3,2)
_,cnt2,hier2 = cv2.findContours(th2,3,2)

cv2.drawContours(img,[cnt1[2]],-1,(255,0,0),2)
cv2.drawContours(img2,[cnt2[7]],-1,(255,0,0),2)
ret = cv2.matchShapes(cnt1[2],cnt2[7],1,0.0) #需要搞清楚，究竟哪个才是你需要的轮廓
print(ret)
cv2.imshow("cnt1",img)
cv2.imshow("cnt2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

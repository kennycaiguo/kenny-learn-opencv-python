import cv2
import numpy as np
# 平均颜色
img = cv2.imread('../../mydata/tubao.jpeg')  # 填写图片名称
cv2.imshow("original", img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,th = cv2.threshold(gray,235,255,cv2.THRESH_BINARY)
_,contours,hierary = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
mask = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask,[cnt],-1,(255,255,0),3)
mean_val = cv2.mean(gray,mask=mask)
print("Mean Value:",mean_val)
cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

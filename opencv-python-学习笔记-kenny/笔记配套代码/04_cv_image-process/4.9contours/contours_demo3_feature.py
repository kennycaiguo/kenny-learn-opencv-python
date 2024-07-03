import cv2
import numpy as np

img = cv2.imread('../mydata/star.png',0)  # 这里需要灰度图片
ret,th = cv2.threshold(img,127,255,0)
_,contours,hierarchy = cv2.findContours(th,1,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
M = cv2.moments(cnt) #1.轮廓的矩
print(M)
area = cv2.contourArea(cnt) # 2.轮廓面积
print("contours area:",area)
perimeter = cv2.arcLength(cnt,True) # 3.轮廓周长
print('perimeter:',perimeter)
cv2.waitKey(0)
cv2.destroyAllWindows()

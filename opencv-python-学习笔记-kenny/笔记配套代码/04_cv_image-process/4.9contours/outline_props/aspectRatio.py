import cv2
import numpy as np

img = cv2.imread('../../mydata/tubao.jpeg')  # 填写图片名称
cv2.imshow("original", img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 二值化，取阈值为235
ret,th = cv2.threshold(gray,235,255,cv2.THRESH_BINARY)
# 查找轮廓
_,contours,hierary = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
x,y,w,h = cv2.boundingRect(cnt)
#计算宽高比
aspect_ratio = float(w)/h
print("Aspect Ratio",aspect_ratio)
img2 = img.copy()
cv2.rectangle(img2,(x,y),(x+w,y+h),(255,255,0),3)
cv2.imshow("Result", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

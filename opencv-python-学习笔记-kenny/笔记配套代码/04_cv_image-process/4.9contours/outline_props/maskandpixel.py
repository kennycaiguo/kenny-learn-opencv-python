import cv2
import numpy as np

img = cv2.imread('../../mydata/tubao.jpeg')  # 填写图片名称
cv2.imshow("original", img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 二值化，取阈值为235
ret,th = cv2.threshold(gray,235,255,cv2.THRESH_BINARY)
# 查找轮廓
_,contours,hierary = cv2.findContours(th,2,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
mask = np.zeros(img.shape,np.uint8)
cv2.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
print('Pixel Points:' , pixelpoints)
cv2.imshow('Result',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

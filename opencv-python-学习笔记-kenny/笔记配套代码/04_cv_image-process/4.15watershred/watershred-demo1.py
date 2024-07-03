import cv2
import numpy as np

img = cv2.imread('../mydata/coins.jpeg')  # 填写图片名称
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 二值化
ret0,th0 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#开操作
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(th0,cv2.MORPH_OPEN,kernel,iterations=2)
# 膨胀操作，确定背景区域
sure_bg = cv2.dilate(opening,kernel,iterations=3)
# 确定前景区域
d_trans = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret1,sure_fg = cv2.threshold(d_trans,0.7*d_trans.max(),255,0)
# 查找未知区域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
# 从确定前景在获取标记标签
ret2,markers1 = cv2.connectedComponents(sure_fg)
markers2 = markers1+1
markers2[unknown==255] = 0
# 分水岭操作
markers3 = cv2.watershed(img,markers2)
img[markers3==-1] = [0,255,0]
cv2.imshow('thresh0',th0)
cv2.imshow('sure_bg', sure_bg)
cv2.imshow('sure_fg', sure_fg)
cv2.imshow('result_img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

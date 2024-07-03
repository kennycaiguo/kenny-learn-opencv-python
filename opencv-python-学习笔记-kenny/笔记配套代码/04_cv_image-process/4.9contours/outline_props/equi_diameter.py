import cv2
import numpy as np
"""
equi_diameter:等效直径，计算方法： np.sqrt(4*area/np.pi) np是numpy的缩写

"""

img = cv2.imread('../../mydata/tubao.jpeg')  # 填写图片名称
cv2.imshow("original", img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 二值化，取阈值为235
ret,th = cv2.threshold(gray,235,255,cv2.THRESH_BINARY)
# 查找轮廓
_,contours,hierary = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
# 计算轮廓面积
area = cv2.contourArea(cnt)
# 计算等效直径
equal_diameter = np.sqrt(4*area/np.pi)
print("Equal Diameter:",equal_diameter)
cv2.waitKey(0)
cv2.destroyAllWindows()

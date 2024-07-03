import cv2
import numpy as np
"""
方向

其实际上就是指物体指向的角度，我们在之前的椭圆拟合里就讲过，它会返回三个参数：主轴和短轴长度以及角度
"""

img = cv2.imread('../../mydata/tubao.jpeg')  # 填写图片名称
cv2.imshow("original", img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 二值化，取阈值为235
ret,th = cv2.threshold(gray,235,255,cv2.THRESH_BINARY)
# 查找轮廓
_,contours,hierary = cv2.findContours(th,2,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
# 计算方向，其实就是角度
(x,y),(Ma,ma),angle = cv2.fitEllipse(cnt)
print("Angle:",angle)
cv2.waitKey(0)
cv2.destroyAllWindows()

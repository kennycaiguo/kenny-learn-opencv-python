import cv2
import numpy as np
"""
极值点表示对象的最顶部，最底部，最右侧和最左侧的点。
"""
img = cv2.imread('../../mydata/tubao.jpeg')  # 填写图片名称
cv2.imshow("original", img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 二值化，取阈值为235
ret,th = cv2.threshold(gray,235,255,cv2.THRESH_BINARY)
# 查找轮廓
_,contours,hierary = cv2.findContours(th,2,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
# 计算极点
left_most = tuple(cnt[cnt[:,:,0].argmin()][0])
right_most = tuple(cnt[cnt[:,:,0].argmax()][0])
left_most = tuple(cnt[cnt[:,:,0].argmin()][0])
top_most = tuple(cnt[cnt[:,:,1].argmin()][0])
bottm_most = tuple(cnt[cnt[:,:,1].argmax()][0])
cv2.circle(img,left_most,2,(0,0,255),5)
cv2.circle(img,right_most,2,(0,255,255),5)
cv2.circle(img,top_most,2,(0,255,0),5)
cv2.circle(img,bottm_most,2,(255,0,255),5)
cv2.imshow("xx most", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

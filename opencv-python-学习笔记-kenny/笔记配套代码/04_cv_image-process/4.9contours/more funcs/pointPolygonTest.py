from __future__ import print_function,division
import cv2
import numpy as np

#创建一幅图片
r = 100
src = np.zeros((4*r,4*r),np.uint8)
#创建6个顶点
# 创建六边形的6个顶点
vert = [None]*6
vert[0] = (3*r//2, int(1.34*r))
vert[1] = (1*r, 2*r)
vert[2] = (3*r//2, int(2.866*r))
vert[3] = (5*r//2, int(2.866*r))
vert[4] = (3*r, 2*r)
vert[5] = (5*r//2, int(1.34*r))
# 根据六个顶点画6边形
for i in range(6):
    cv2.line(src,vert[i],vert[(i+1)%6],(255),3)
# 轮廓查找
_,contours,_ = cv2.findContours(src,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# 计算图上点到六边形的距离（带符号）
raw_dist = np.empty(src.shape,dtype=np.float32)
for i in range(src.shape[0]):
    for j in range(src.shape[1]):
        raw_dist[i,j] = cv2.pointPolygonTest(contours[0],(j,i),True)
        # 查找最大值和最小值
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(raw_dist)
minVal = abs(min_val)
maxVal = abs(max_val)
drawing = np.zeros((src.shape[0],src.shape[1],3),np.uint8)
for i in range(src.shape[0]):
    for j in range(src.shape[1]):
        if raw_dist[i,j] < 0:
            drawing[i,j,0] = 255 - abs(raw_dist[i,j])*255/minVal
        elif raw_dist[i,j] > 0:
            drawing[i,j,2] = 255 - abs(raw_dist[i,j])*255/maxVal
        else:
            drawing[i, j, 0] = 255
            drawing[i, j, 1] = 255
            drawing[i, j, 2] = 255
cv2.circle(drawing,max_loc,int(maxVal),(0,0,255),2)
cv2.imshow('Source',src)
cv2.imshow('Distance and inscribed circle',drawing)
cv2.waitKey(0)
cv2.destroyAllWindows()

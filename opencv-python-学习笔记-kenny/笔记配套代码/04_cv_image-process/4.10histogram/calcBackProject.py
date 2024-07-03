import cv2
import numpy as np

target = cv2.imread('../mydata/road.png')  # 填写图片名称
cv2.imshow("original", target)
sample = cv2.imread('../mydata/road_sample.png')
# 转化为hsv颜色空间
hsv_target = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
hsv_sample = cv2.cvtColor(sample,cv2.COLOR_BGR2HSV)

# 绘制直方图,这里histSize不能设置太大，使用[20,32]就可以了
roiHist = cv2.calcHist([hsv_sample],[0,1],None,[20,32],[0,180,0,256])
# 归一化
roiHist = cv2.normalize(roiHist,roiHist,0,255,cv2.NORM_MINMAX)
proImage = cv2.calcBackProject([hsv_target],[0,1],roiHist,[0,180,0,256],1.0)
cv2.imshow("back project", proImage)

cv2.waitKey(0)
cv2.destroyAllWindows()

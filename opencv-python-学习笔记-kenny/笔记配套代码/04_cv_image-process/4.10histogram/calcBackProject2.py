import cv2
import numpy as np

# target = cv2.imread('../mydata/rose.jpeg')  # 填写图片名称
target = cv2.imread('../mydata/messi5.jpg')  # 填写图片名称
target = cv2.resize(target,(400,250))
# cv2.imshow("original", target)
# sample = cv2.imread('../mydata/rose_red.jpeg')
sample = cv2.imread('../mydata/green_sample.png')
# 转化为hsv颜色空间
hsv_target = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
hsv_sample = cv2.cvtColor(sample,cv2.COLOR_BGR2HSV)

# 绘制直方图,这里histSize不能设置太大，使用[20,32]就可以了
roiHist = cv2.calcHist([hsv_sample],[0,1],None,[180,256],[0,180,0,256])
# 归一化
roiHist = cv2.normalize(roiHist,roiHist,0,255,cv2.NORM_MINMAX)
proImage = cv2.calcBackProject([hsv_target],[0,1],roiHist,[0,180,0,256],1.0)
# Now convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
dst = cv2.filter2D(proImage,-1,disc)
# threshold and binary AND
ret,thresh = cv2.threshold(dst,50,255,0)
thresh = cv2.merge((thresh,thresh,thresh))
res = cv2.bitwise_and(target,thresh)
res = np.hstack((target,thresh,res))
cv2.imshow("result", res)
cv2.waitKey(0)
cv2.destroyAllWindows()

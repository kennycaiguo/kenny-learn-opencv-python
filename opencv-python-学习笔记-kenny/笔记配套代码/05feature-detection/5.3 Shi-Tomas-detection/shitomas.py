import cv2
import numpy as np


img = cv2.imread('../pic_datas/blox.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
"""
shi-tomas使用的api是：goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance, 
        corners=None, mask=None, blockSize=None, useHarrisDetector=None, k=None)
"""
corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)
# 遍历角点
for c in corners:
    x,y = c.ravel()
    cv2.circle(img,(x,y),2,(0,0,255),-1)
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

img = cv2.imread('../pic_datas/home.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#创建sift对象
sift = cv2.xfeatures2d_SIFT.create()
# kp = sift.detect(gray,None) # ok
# kp,des = sift.compute(gray,None) #不好
kp,des = sift.detectAndCompute(gray,None)
img2 = cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
OpenCV也提供了绘制关键点的函数：cv2.drawKeyPoints()，它可以在关键点的部位绘制一个小圆圈。
如果你设置参数为cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS，就会绘制代表关键点大小的圆圈甚至可以绘制除关键点的方向。
"""
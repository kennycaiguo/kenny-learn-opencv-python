import cv2
import numpy as np

img = cv2.imread('../pic_datas/home.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#创建sift对象
sift = cv2.xfeatures2d_SIFT.create()
kp = sift.detect(gray,None)
img2 = cv2.drawKeypoints(gray,kp,img)
cv2.imshow("result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

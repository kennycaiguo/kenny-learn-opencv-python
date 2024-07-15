import cv2
import numpy as np

img = cv2.imread('../pic_datas/blox.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Initiate ORB detector
orb = cv2.ORB_create()
# find the keypoints with ORB
kp = orb.detect(gray,None)
# compute the descriptors with ORB
kp,des = orb.compute(gray,kp)
# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(gray,kp,img,(0,255,0),flags=0)
cv2.imshow("result", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

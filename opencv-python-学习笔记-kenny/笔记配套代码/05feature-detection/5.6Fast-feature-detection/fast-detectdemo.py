import cv2
import numpy as np

img = cv2.imread('../pic_datas/blox.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("pic", img)
fast = cv2.FastFeatureDetector_create()
kp = fast.detect(gray)
gray2 = gray.copy()
gray2 = cv2.drawKeypoints(gray,kp,None,color=(255,0,0))
# Print all default params
print( "Threshold: {}".format(fast.getThreshold()) )
print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
print( "neighborhood: {}".format(fast.getType()) )
print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )
cv2.imshow('fast_true',gray2)
gray3 = gray.copy()

# Disable nonmaxSuppression 关闭非最大值抑制
fast.setNonmaxSuppression(0)
kp = fast.detect(gray)
gray3 = cv2.drawKeypoints(gray,kp,None,color=(255,0,0))
cv2.imshow('fast_false',gray3)
cv2.waitKey(0)
cv2.destroyAllWindows()

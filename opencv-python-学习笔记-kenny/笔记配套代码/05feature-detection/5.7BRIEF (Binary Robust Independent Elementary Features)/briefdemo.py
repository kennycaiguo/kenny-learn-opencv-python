import cv2
import numpy as np

img = cv2.imread('../pic_datas/blox.jpg',0)  # 以灰度方式读入
# Initiate FAST detector
star = cv2.xfeatures2d.StarDetector_create()
# Initiate BRIEF extractor
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
# find the keypoints with STAR
kp = star.detect(img,None)
# compute the descriptors with BRIEF
kp,des = brief.compute(img,kp)
print( brief.descriptorSize() )
print( des.shape )
img2 = cv2.drawKeypoints(img,kp,None,color=(0,255,0))

cv2.imshow("result", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

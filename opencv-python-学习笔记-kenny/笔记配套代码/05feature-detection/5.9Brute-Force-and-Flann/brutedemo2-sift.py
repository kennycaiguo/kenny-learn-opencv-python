import cv2
import numpy as np

img1 = cv2.imread('../pic_datas/box.png',0)  # 填写图片名称
img2 = cv2.imread('../pic_datas/box_in_scene.png',0)  # 填写图片名称

# 创建orb对象
orb = cv2.ORB_create()
# find the keypoints and descriptors with ORB
kp1,des1 = orb.detectAndCompute(img1,None)
kp2,des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)  # 注意：这里如果没有参数，最后得到的结构不一样
# Match descriptors.
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches,key=lambda x:x.distance)
# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=2)
cv2.imshow('Result',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

img1 = cv2.imread('../pic_datas/box.png',0)  # 填写图片名称
img2 = cv2.imread('../pic_datas/box_in_scene.png',0)  # 填写图片名称

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()
# find the keypoints and descriptors with ORB
kp1,des1 = sift.detectAndCompute(img1,None)
kp2,des2 = sift.detectAndCompute(img2,None)
# FLANN parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
search_params = dict(checks=50) # 也可以用空字典dict()
flann = cv2.FlannBasedMatcher(index_params,search_params)
# Match descriptors.
matches = flann.knnMatch(des1,des2,k=2)
# Need to draw only good matches, so create a mask
matchesMask = [[0,0] for i in range(len(matches))]
for i,(m,n) in enumerate(matches):
    if m.distance < 0.7*n.distance :
        matchesMask[i] = [1, 0]
# 定义应该绘制参数字典
draw_params = dict(
    matchColor=(0,255,0),
    singlePointColor=(255,0,0),
    matchesMask=matchesMask,
    flags=0
)
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
cv2.imshow('Result',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

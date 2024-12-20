import cv2
import numpy as np
from matplotlib import pyplot as plt

# 定义一个函数将找到的极线绘制到图像中
def drawlines(img1,img2,lines,pts1,pts2):
    ''' img1 - image on which we draw the epilines for the points in img2
        lines - corresponding epilines '''
    r,c = img1.shape
    img1 = cv2.cvtColor(img1,cv2.COLOR_GRAY2BGR)
    img2 = cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)
    for r,pt1,pt2 in zip(lines,pts1,pts2):
        color = tuple(np.random.randint(0,255,3).tolist())
        x0,y0 = map(int, [0, -r[2]/r[1] ])
        x1,y1 = map(int, [c, -(r[2]+r[0]*c)/r[1] ])
        img1 = cv2.line(img1, (x0,y0), (x1,y1), color,1)
        img1 = cv2.circle(img1,tuple(pt1),5,color,-1)
        img2 = cv2.circle(img2,tuple(pt2),5,color,-1)
    return img1,img2

img1 = cv2.imread('./left.jpg',0)  # queryimage # left image,查询图片，灰度的
img2 = cv2.imread('./right.jpg',0) #trainimage # right image，训练图片，灰度的

# 创建sift对象
sift = cv2.xfeatures2d.SIFT_create()
# find the keypoints and descriptors with SIFT，用sift算法寻找关键点
kp1,des1 = sift.detectAndCompute(img1,None)
kp2,des2 = sift.detectAndCompute(img2,None)
# 设置FLANN 参数
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
search_params = dict(checks=50)
#创建flann对象
flann = cv2.FlannBasedMatcher(index_params,search_params)
# 特征匹配
matches = flann.knnMatch(des1,des2,k=2)
good=[]
pts1=[]
pts2=[]
#遍历匹配结果，找到好的特征
for i,(m,n) in enumerate(matches):
    if m.distance < 0.8*n.distance:
        good.append(m)
        pts1.append(kp1[m.queryIdx].pt) #保存查询点
        pts2.append(kp2[m.trainIdx].pt) #保存训练点
#找到基本矩阵
pts1=np.int32(pts1)
pts2=np.int32(pts2)
F,mask = cv2.findFundamentalMat(pts1,pts2,cv2.FM_LMEDS)
# 我们只选择内点群inlier的点
pts1 = pts1[mask.ravel()==1]
pts2 = pts2[mask.ravel()==1]

# 要找到极线。我们会得到一个包含很多线的数组。所以我们要调用上面的函数将这些线绘制到图像中。
# Find epilines corresponding to points in right image (second image) and
# drawing its lines on left image 先做右边的
lines1 = cv2.computeCorrespondEpilines(pts2.reshape(-1,1,2),2,F)
lines1 = lines1.reshape(-1,3)
img5,img6 = drawlines(img1,img2,lines1,pts1,pts2)

#再做左边的
lines2 = cv2.computeCorrespondEpilines(pts1.reshape(-1,1,2),1,F)
lines2 = lines2.reshape(-1,3)
img3,img4 = drawlines(img2,img1,lines2,pts2,pts1)
plt.subplot(121),plt.imshow(img5)
plt.subplot(122),plt.imshow(img3)
plt.show()
# cv2.imshow("pic", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

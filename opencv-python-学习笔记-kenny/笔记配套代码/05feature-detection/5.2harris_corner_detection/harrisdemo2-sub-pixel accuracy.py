import cv2
import numpy as np

img = cv2.imread('../pic_datas/chessboard-2.png')
# 图片太大，需要缩小
# img = cv2.resize(img,(600,480))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
#角点检测
dst = cv2.cornerHarris(gray,2,3,0.04)
#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
# 二值化
ret, dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)
dst = np.uint8(dst)

# find centroids
# connectedComponentsWithStats(InputArray image, OutputArray labels, OutputArray stats,
# OutputArray centroids, int connectivity=8, int ltype=CV_32S)
ret,labels,stat,centerids = cv2.connectedComponentsWithStats(dst)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,100,0.001)
# Python: cv2.cornerSubPix(image, corners, winSize, zeroZone, criteria)
# zeroZone – Half of the size of the dead region in the middle of the search zone
# over which the summation in the formula below is not done. It is used sometimes
# to avoid possible singularities of the autocorrelation matrix. The value of (-1,-1)
# indicates that there is no such a size.
# 返回值由 点坐标组成的一个数组
corners = cv2.cornerSubPix(gray,np.float32(centerids),(3,3),(-1,-1),criteria)

# Now draw them
res = np.hstack((centerids,corners))
# np.int0 可以用来省略小数点后的数字，非四舍五入
res = np.int0(res)
img[res[:, 1], res[:, 0]] = [0, 0, 255]
img[res[:, 3], res[:, 2]] = [0, 255, 0]

cv2.imshow('subpixel5.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
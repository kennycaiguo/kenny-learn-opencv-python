import cv2
import numpy as np
import glob

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_MAX_ITER,30,0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3),np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imagepoints = [] # 2d points in image plane.
# 批量获取当前文件夹下面的jpg文件路径
images = glob.glob('*.jpg')
# 变量路径列表
for fname in images:
    #读取图片，并且转化为灰度图
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret,corners = cv2.findChessboardCorners(gray,(7,6),None)
    # If found, add object points, image points (after refining them)
    if ret:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imagepoints.append(corners)
        # Draw and display the corners
        cv2.drawChessboardCorners(img,(7,6),corners2,ret)
        cv2.imshow("pic", img)
        cv2.waitKey(0)


cv2.destroyAllWindows()

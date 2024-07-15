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
        # cv2.imshow("pic", img)
        # 做摄像机标定
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints,imagepoints,gray.shape[::-1],None,None)
#保存上面的矫正的结果，使用命名参数保存法
np.savez('b2.npz',ret=ret, mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)
#我们读取一个新的图像
img = cv2.imread('left12.jpg')
h,  w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
# undistort
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult.png', dst)
cv2.waitKey(0)


cv2.destroyAllWindows()

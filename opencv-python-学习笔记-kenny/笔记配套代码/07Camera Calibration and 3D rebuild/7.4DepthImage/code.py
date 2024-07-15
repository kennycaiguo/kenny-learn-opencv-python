import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgL = cv.imread('./tsukuba_l.png',0)
imgR = cv.imread('./tsukuba_r.png',0)

# disparity range is tuned for 'aloe' image pair
window_size = 3
min_disp = 16
num_disp = 112 - min_disp
stereo = cv.StereoSGBM_create(minDisparity=min_disp,
                              numDisparities=num_disp,
                              blockSize=16,
                              P1=8 * 3 * window_size ** 2,
                              P2=32 * 3 * window_size ** 2,
                              disp12MaxDiff=1,
                              uniquenessRatio=10,
                              speckleWindowSize=100,
                              speckleRange=32
                              )

print('computing disparity...')
# disp = stereo.compute(imgL, imgR).astype(np.float32) / 16.0
disp = stereo.compute(imgR, imgL).astype(np.float32)/16.0 # 有时候反过来效果更好


plt.imshow(disp,'gray')
plt.show()
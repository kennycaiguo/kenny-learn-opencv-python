import cv2
import numpy as np

img = cv2.imread('../pic_datas/chessboard.png')
# 图片太大，需要缩小
img = cv2.resize(img,(600,480))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
#角点检测
dst = cv2.cornerHarris(gray,2,3,0.04)
#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
# Threshold for an optimal value, it may vary depending on the image.
img[dst > 0.01 * dst.max()] = [0,0,255]
cv2.imshow('result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
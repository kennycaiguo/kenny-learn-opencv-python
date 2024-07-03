import cv2
import numpy as np

img = cv2.imread('sudoku2.png')  # 填写图片名称
rows,cols,chs = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]]) # 选取的变换之前的点
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]]) # 变换目标点

# 获取透视矩阵
m = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,m,(rows,cols))
cv2.imshow("original", img)
cv2.imshow("perspective", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

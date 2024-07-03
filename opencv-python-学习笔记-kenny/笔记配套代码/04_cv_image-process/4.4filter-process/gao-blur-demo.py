import cv2
import numpy as np


# img = cv2.imread('../mydata/opencv-logo-white.png')  # 填写图片名称
img = cv2.imread('../mydata/cv-logo-noisy.jpeg')  # 填写图片名称
gblur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("original", img)
cv2.imshow("filtered", gblur)

cv2.waitKey(0)
cv2.destroyAllWindows()

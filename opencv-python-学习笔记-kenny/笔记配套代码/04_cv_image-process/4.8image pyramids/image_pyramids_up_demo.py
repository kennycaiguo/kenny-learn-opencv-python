import cv2
import numpy as np


img = cv2.imread('../mydata/messi5.jpg')  # 填写图片名称
img2 = cv2.resize(img,(180,120))
up1 = cv2.pyrUp(img2)
up2 = cv2.pyrUp(up1)

cv2.imshow('org',img2)
cv2.imshow('once',up1)
cv2.imshow('twice',up2)


cv2.waitKey(0)
cv2.destroyAllWindows()

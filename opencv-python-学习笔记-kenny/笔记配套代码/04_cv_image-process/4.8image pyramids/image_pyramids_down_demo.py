import cv2
import numpy as np


img = cv2.imread('../mydata/messi5.jpg')  # 填写图片名称
down1 = cv2.pyrDown(img)
down2 = cv2.pyrDown(down1)

cv2.imshow('org',img)
cv2.imshow('once',down1)
cv2.imshow('twice',down2)


cv2.waitKey(0)
cv2.destroyAllWindows()

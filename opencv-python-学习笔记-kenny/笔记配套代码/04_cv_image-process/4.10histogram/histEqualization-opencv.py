import cv2
import numpy as np

img = cv2.imread('../mydata/wiki.jpg',0)  # 以灰度方式读取图片
img = cv2.resize(img,(500,480))
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))

cv2.imshow('result',res)
cv2.imwrite('result.png',res)

cv2.waitKey(0)
cv2.destroyAllWindows()

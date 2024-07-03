import cv2
import numpy as np

img = cv2.imread('opencv-logo-small.png')  # 填写图片名称
# img2 = cv2.resize(img,(150,200))
# cv2.imwrite("./opencv-logo-small.png",img2)
replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=[255,255,0])
# cv2.imshow("pic", img)
cv2.imshow('orginal',img)
cv2.imshow("pic", np.hstack((replicate,reflect,reflect101,wrap,constant)))

cv2.waitKey(0)
cv2.destroyAllWindows()

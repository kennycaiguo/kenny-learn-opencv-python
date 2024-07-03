import cv2
import numpy as np

img = cv2.imread('../mydata/map-carpet.jpeg')  # 填写图片名称
bblur = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("original", img)
cv2.imshow("filtered", bblur)

cv2.waitKey(0)
cv2.destroyAllWindows()

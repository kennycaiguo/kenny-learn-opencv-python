import cv2
import numpy as np

img = cv2.imread('../mydata/tsukuba_l.png',0)  # 填写图片名称
cv2.imshow('original',img)
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
res = clahe.apply(img)
cv2.imshow("Result", res)
cv2.imwrite('tsukuba_en.png',res)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

img = cv2.imread('../mydata/arr-drawing.png')  # 填写图片名称
cv2.imshow("original", img)
rows,cols,chs = img.shape
pt1 = np.float32([[50,50],[200,50],[50,200]])
pt2 = np.float32([[10,100],[200,50],[100,250]])
matrix = cv2.getAffineTransform(pt1,pt2)
ret = cv2.warpAffine(img,matrix,(cols,rows))
cv2.imshow("result", ret)

cv2.waitKey(0)
cv2.destroyAllWindows()

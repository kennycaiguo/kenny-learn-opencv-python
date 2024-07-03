import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../mydata/home.jpg')  # 填写图片名称
cv2.imshow("pic", img)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) # 转化为hsv颜色空间
h,s,v = cv2.split(hsv)
hist, xbins, ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])
plt.imshow(hist,interpolation = 'nearest')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

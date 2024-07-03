import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../mydata/wiki.jpg',0)  # 以灰度方式读取图片
img = cv2.resize(img,(500,480))
# cv2.imshow('gray',img)
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
#做转换
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')

#保存增强后的图像
img2 = cdf[img]
cv2.imwrite('wiki_enhanced.png',img2)
cv2.imshow('img2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

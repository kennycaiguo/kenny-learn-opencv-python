import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('../mydata/wiki.jpg',0)  # 以灰度方式读取图片
img = cv2.imread('./wiki_enhanced.png',0)  # 以灰度方式读取图片
# img = cv2.resize(img,(500,480))
cv2.imshow('gray',img)
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max())/cdf.max()
plt.plot(cdf_normalized,color = 'b')
plt.hist(img.flatten(),256,[0,256],color='r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

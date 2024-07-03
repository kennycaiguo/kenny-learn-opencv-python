import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../mydata/opencv-logo-white.png')  # 填写图片名称
kernel = np.ones((5,5),np.float32) / 25 # 获取卷积核
ret = cv2.filter2D(img,-1,kernel)
# cv2.imshow("original", img)
# cv2.imshow("filtered", ret)
plt.subplot(121),plt.imshow(img),plt.title("Original")
plt.subplot(122),plt.imshow(ret),plt.title("Filtered")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

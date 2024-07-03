import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../mydata/letterj-spotted.jpeg', )  # 填写图片名称
kernel = np.ones((11,11),np.uint8) # 卷积核需要慢慢调整太小了清除不干净
closed_img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

plt.subplot(121),plt.imshow(img),plt.title("Original")
plt.subplot(122),plt.imshow(closed_img),plt.title("closed_img")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

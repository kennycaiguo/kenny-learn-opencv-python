import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../mydata/letterj.png',)  # 填写图片名称
kernel = np.ones((5,5),np.uint8)
erode_img = cv2.erode(img,kernel)
# cv2.imshow("pic", img)
# cv2.imshow("eroded", erode_img)
plt.subplot(121),plt.imshow(img),plt.title("Original")
plt.subplot(122),plt.imshow(erode_img),plt.title("Eroded")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

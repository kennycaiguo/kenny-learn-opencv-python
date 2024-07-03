import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../mydata/cv-logo-noisy.jpeg')  # 填写图片名称
blur = cv2.medianBlur(img,5)
# cv2.imshow("original", img)
# cv2.imshow("filtered", ret)
plt.subplot(121),plt.imshow(img),plt.title("Original")
plt.subplot(122),plt.imshow(blur),plt.title("Blured")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

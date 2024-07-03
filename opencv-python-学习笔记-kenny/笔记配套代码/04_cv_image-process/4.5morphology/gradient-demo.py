import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../mydata/letterj.png',)  # 填写图片名称
kernel = np.ones((5,5),np.uint8)
gra_img = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel) # 结果有点像轮廓
# cv2.imshow("pic", img)
# cv2.imshow("eroded", erode_img)
plt.subplot(121),plt.imshow(img),plt.title("Original")
plt.subplot(122),plt.imshow(gra_img),plt.title("Gradient")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

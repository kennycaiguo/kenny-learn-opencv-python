import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../mydata/letterj.png',)  # 填写图片名称
kernel = np.ones((9,9),np.uint8) # 用9x9卷积核效果比较好
bhat_img = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel) # 结果有点像轮廓
# cv2.imshow("pic", img)
# cv2.imshow("eroded", erode_img)
plt.subplot(121),plt.imshow(img),plt.title("Original")
plt.subplot(122),plt.imshow(bhat_img),plt.title("Black hat")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

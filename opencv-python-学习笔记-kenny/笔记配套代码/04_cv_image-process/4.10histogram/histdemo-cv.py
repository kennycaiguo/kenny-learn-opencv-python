import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../mydata/home.jpg',0)  # 填写图片名称
mask = np.zeros(img.shape[:2],np.uint8)
mask[100:300,100:400] = 255 # 在蒙版中设置看见区域
masked = cv2.bitwise_and(img,img,mask=mask)
hist_full = cv2.calcHist([img],[0],None,[256],[0,255])
hist_mask = cv2.calcHist([masked],[0],mask,[256],[0,256])
plt.subplots_adjust(hspace=0.5)
plt.subplot(2,2,1),plt.imshow(img,'gray'),plt.title('Original')
plt.subplot(2,2,2),plt.imshow(mask,'gray'),plt.title('Mask')
plt.subplot(2,2,3),plt.imshow(masked,'gray'),plt.title('Masked Image')
plt.subplot(2,2,4),plt.plot(hist_full),plt.plot(hist_mask),plt.title('Histograms')
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

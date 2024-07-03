import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../mydata/opencv-logo-white.png')  # 填写图片名称
ret1 = cv2.boxFilter(img,-1,(5,5),normalize=True)
ret2 = cv2.boxFilter(img,-1,(5,5),normalize=False)

plt.subplots_adjust(wspace=0.5,hspace=0)
plt.subplot(131),plt.imshow(img),plt.title("Original")
plt.subplot(132),plt.imshow(ret1),plt.title("boxFiltered--flag True")
plt.subplot(133),plt.imshow(ret2),plt.title("boxFiltered--flag False")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

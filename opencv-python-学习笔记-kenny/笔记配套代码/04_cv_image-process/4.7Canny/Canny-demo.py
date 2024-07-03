import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../mydata/messi5.jpg',0)  # 注意边缘检测需要使用灰度图否则非常慢
edge = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap='gray'),plt.title('Original') # 用灰度模式显示否则非常丑
plt.subplot(122),plt.imshow(edge,cmap='gray'),plt.title('Canny result')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

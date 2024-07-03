import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../mydata/home.jpg',0)  # 填写图片名称
plt.hist(img.ravel(),256,[0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

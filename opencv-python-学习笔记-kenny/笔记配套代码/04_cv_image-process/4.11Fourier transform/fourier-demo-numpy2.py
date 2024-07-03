import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../mydata/messi5.jpg',0)  # 需要以灰度图的方式加载
rows,cols = img.shape
crows,ccols = int(rows/2),int(cols/2)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
fshift[crows-30:crows+30,ccols-30:ccols+30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

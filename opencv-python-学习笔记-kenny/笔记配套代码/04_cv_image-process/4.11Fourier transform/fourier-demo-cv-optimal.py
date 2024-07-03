import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../mydata/messi5.jpg',0)  # 需要以灰度图的方式加载
rows,cols = img.shape
# 获取最佳行数和列数
nrows = cv2.getOptimalDFTSize(rows)
ncols = cv2.getOptimalDFTSize(cols)
# 图片转换
nimg = np.zeros((nrows,ncols))
nimg[:rows,:cols] = img
#
dft =cv2.dft(np.float32(nimg),flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft[:,:,0],dft[:,:,1]))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

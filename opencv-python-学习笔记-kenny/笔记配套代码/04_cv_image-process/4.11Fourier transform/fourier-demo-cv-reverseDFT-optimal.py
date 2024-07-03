import cv2
import numpy as np
# 性能优化，代价是多了一些不需要的像素

from matplotlib import pyplot as plt
img = cv2.imread('../mydata/messi5.jpg',0)  # 需要以灰度图的方式加载
rows,cols = img.shape
# 获取最佳行数和列数
nrows = cv2.getOptimalDFTSize(rows)
ncols = cv2.getOptimalDFTSize(cols)
# 图片转换
nimg = np.zeros((nrows,ncols))
nimg[:rows,:cols] = img

cnrows ,cncols = int(nrows/2),int(ncols/2)
mask = np.zeros((nrows,ncols,2),np.uint8)
mask[cnrows-30:cnrows+30, cncols-30:cncols+30] = 1
# apply mask and inverse DFT
dft =cv2.dft(np.float32(nimg),flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
f_shift = dft_shift * mask
f_ishift = np.fft.ifftshift(f_shift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
from matplotlib import pyplot as plt
# 这是不好的
img = cv2.imread('../mydata/messi5.jpg')  # 填写图片名称
# 创建mask
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50,50,450,290)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,iterCount=5,mode=cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
cv2.imshow("pic", img)
plt.imshow(img), plt.colorbar(), plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

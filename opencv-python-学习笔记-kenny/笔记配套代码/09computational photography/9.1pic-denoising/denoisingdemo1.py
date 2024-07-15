# -*- encoding:utf-8 -*-
# @日期和时间：2024/7/14 18:14
# @Author: Kenny cai
# @File name:denoisingdemo1.py
# @dev tool:PyCharm

#
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./cv-logo-noisy.jpeg')
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()
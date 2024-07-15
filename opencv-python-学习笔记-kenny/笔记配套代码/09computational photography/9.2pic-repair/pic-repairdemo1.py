# -*- encoding:utf-8 -*-
# @日期和时间：2024/7/14 18:44
# @Author: Kenny cai
# @File name:pic-repairdemo1.py
# @dev tool:PyCharm

"""
　我们要创建一个与输入图像大小相等的掩模图像，将待修复区域的像素设置为 255（其他地方为 0）。所有的操作都很简单。
我要修复的图像中有几个黑色笔画。我是使用画笔工具添加的。
"""
import numpy as np
import cv2

img = cv2.imread('messi_2.jpg')
mask = cv2.imread('mask2.png',0)

dst = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
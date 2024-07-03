# -*- coding: UTF-8 -*-
import cv2 as cv
import numpy as np


def watershed_algorithm(image):
    # 边缘保留滤波EPF  去噪
    blur = cv.pyrMeanShiftFiltering(image,sp=10,sr=100)
    # 转成灰度图像
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    # 得到二值图像   自适应阈值
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # cv.imshow('binary image', binary)

    # 形态学操作   获取结构元素  开操作
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    opening = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel=kernel, iterations=2)
    # 确定区域
    sure_bg = cv.dilate(opening, kernel, iterations=3)
    # cv.imshow('mor-opt', sure_bg)

    # 距离变换
    dist = cv.distanceTransform(opening, cv.DIST_L2, 3)
    dist_out = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    # cv.imshow('distance-', dist_out * 50)
    ret, surface = cv.threshold(dist_out, dist_out.max() * 0.55, 255, cv.THRESH_BINARY)
    # cv.imshow('surface-markers', surface)

    surface_fg = np.uint8(surface)    # 转成8位整型
    unkonown = cv.subtract(sure_bg, surface_fg)        # 找到位置区域
    # Marker labelling
    ret, markers = cv.connectedComponents(surface_fg)  # 连通区域
    print(ret)

    # 分水岭变换
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1
    # Now, mark the region of unknown with zero
    markers[unkonown == 255] = 0
    # 实施分水岭算法了。标签图像将会被修改，边界区域的标记将变为 -1
    markers = cv.watershed(image, markers=markers)
    image[markers == -1] = [0, 0, 255]      # 被标记的区域   设为红色
    cv.imshow('result', image)


src = cv.imread('../mydata/silver_coins.jpeg')
src = cv.resize(src, None, fx=0.5, fy=0.5)
cv.imshow('input image', src)
watershed_algorithm(src)
cv.waitKey(0)
cv.destroyAllWindows()
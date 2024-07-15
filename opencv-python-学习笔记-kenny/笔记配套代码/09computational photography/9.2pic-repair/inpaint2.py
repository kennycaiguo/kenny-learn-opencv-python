# -*- encoding:utf-8 -*-
# @日期和时间：2024/7/14 19:58
# @Author: Kenny cai
# @File name:inpaint2.py
# @dev tool:PyCharm

"""

"""
import cv2
import numpy as np

start_point = (0, 0)  # 鼠标开始坐标
lb_down = False  # 鼠标左键按下的标志，bool型


def mouse_event(event, x, y, flags, param):
    global start_point, end_point, lb_down  # 如果全局变量是int或者str，那么如果想要在函数中对函数变量进行修改，则需要
    # 先在函数内，声明其为global，再进行修改，如果是list或者dict则可以直接修改

    if event == cv2.EVENT_LBUTTONDOWN:  # 左键按下，更新鼠标坐标，启动按下标志
        start_point = (x, y)
        lb_down = True

    elif event == cv2.EVENT_MOUSEMOVE and lb_down:  # 鼠标移动，绘制线
        cv2.line(img, start_point, (x, y), (255, 255, 255), thickness=5)
        cv2.line(mask, start_point, (x, y), (255, 255, 255), thickness=5)
        start_point = (x, y)  # 只要鼠标移动，就更新鼠标的坐标

    elif event == cv2.EVENT_LBUTTONUP:  # 左键释放

        cv2.line(img, start_point, (x, y), (255, 255, 255), thickness=5)  # 鼠标点击后直接释放鼠标的时候也会绘制一个点
        cv2.line(mask, start_point, (x, y), (255, 255, 255), thickness=5)
        lb_down = False


cv2.namedWindow('image')  # 新建窗口，用来进行鼠标操作
img = cv2.imread('./strawberry.png')
mask = np.zeros(img.shape, np.uint8)  # 创建一个黑色mask图像

cv2.setMouseCallback('image', mouse_event)  # 设置鼠标回调

while True:
    cv2.imshow('image', img)
    cv2.imshow('mask', mask)
    k = cv2.waitKey(1)
    if k == ord('q'):  # waitKey参数不能写0，写0就需要键盘输入才会继续
        break
    elif k == 13: # 按回车保存mask，必须注意的是cv2.inpaint里面的mask参数必须是灰度图，否则报错
        cv2.imwrite("smask.png",mask)
    elif k == ord('r') : # 按字母r可以修复图片
        gmask = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
        result = cv2.inpaint(img, gmask, 5, cv2.INPAINT_TELEA)
        cv2.imshow('result', result)

cv2.destroyAllWindows()

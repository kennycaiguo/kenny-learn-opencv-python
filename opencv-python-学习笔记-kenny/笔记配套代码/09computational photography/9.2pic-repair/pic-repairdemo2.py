# -*- encoding:utf-8 -*-
# @日期和时间：2024/7/14 18:44
# @Author: Kenny cai
# @File name:pic-repairdemo1.py
# @dev tool:PyCharm

"""
　https://blog.csdn.net/hzblucky1314/article/details/130517174
"""
import cv2
import numpy as np


def color_restoration(image_path):
    # 读取图像
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # 将图像从 BGR 转换为 LAB
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)

    # 将 LAB 图像拆分为单独的通道
    l_channel, a_channel, b_channel = cv2.split(lab_image)

    # 对每个通道应用自适应直方图均衡化
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    l_channel = clahe.apply(l_channel)
    a_channel = clahe.apply(a_channel)
    b_channel = clahe.apply(b_channel)

    # 将处理后的通道重新组合为 LAB 图像
    lab_image = cv2.merge((l_channel, a_channel, b_channel))

    # 将图像从 LAB 转换回 BGR
    result_image = cv2.cvtColor(lab_image, cv2.COLOR_Lab2BGR)

    return result_image


if __name__ == "__main__":
    input_image_path = "./oldhouse.jpeg"  # 替换为您的老照片路径
    output_image_path = "restored_house.jpg"  # 替换为恢复后的照片路径

    restored_image = color_restoration(input_image_path)
    cv2.imwrite(output_image_path, restored_image)

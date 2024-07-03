import cv2

img = cv2.imread('messi.png')
print(img.shape)  # (283, 450, 3) 高度，宽度，通道数
print(img.size) # 使用img.size获取的像素总数 382050
print(img.dtype) # 使用img.dtype获取图像数据类型 uint8


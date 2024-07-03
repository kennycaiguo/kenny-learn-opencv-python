import cv2
import numpy as np


# img = cv2.imread('../mydata/lena.jpg')  # 填写图片名称
img = cv2.imread('../mydata/messi5.jpg')  # 填写图片名称
print(img.shape)
img = cv2.resize(img,(640,640)) # 拉普拉斯金字塔有一个坑，图像的宽高/2如果是奇数，制作拉普拉斯金字塔就会失败
down1 = cv2.pyrDown(img)
laplace1 = cv2.subtract(img,cv2.pyrUp(down1))
down2 = cv2.pyrDown(down1)
up_down1 = cv2.pyrUp(down2)
laplace2 = cv2.subtract(down1,up_down1)
down3 = cv2.pyrDown(down2)
down4 = cv2.pyrDown(down3)
up_down3 = cv2.pyrUp(down4)
print(down3.shape,up_down3.shape)
laplace3 = cv2.subtract(down3,up_down3)

cv2.imshow('org',img)
cv2.imshow('once',laplace1)
cv2.imshow('twice',laplace2)
cv2.imshow('third',laplace3)


cv2.waitKey(0)
cv2.destroyAllWindows()

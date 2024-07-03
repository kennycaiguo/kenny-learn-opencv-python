import cv2
"""
opencv 图像加法
"""
img = cv2.imread('messi2.png')  # 填写图片名称
b,g,r = cv2.split(img)
img2 = g + r
cv2.imshow("pic", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

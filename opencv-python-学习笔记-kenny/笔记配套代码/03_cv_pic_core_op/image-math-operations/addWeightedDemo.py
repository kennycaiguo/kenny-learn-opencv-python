import cv2
"""
opencv python 图像混合，两个图像的宽高必须完全一样，否则保存
"""
img1 = cv2.imread('ml.png')  # 填写图片名称
img2 = cv2.imread('opencv-logo-small.png')  # 填写图片名称
img = cv2.addWeighted(img1,0.8,img2,0.2,0) # 按权重来混合
cv2.imshow("result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

img = cv2.imread('messi2.png')

roi = img[235:280,275:320] # 截取足球图片
cv2.imshow("ball",roi)
img[235:280, 115:160] = roi # 用足球图片覆盖这个区域
cv2.imshow("messi",img)
# 保存图片
cv2.imwrite("result.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
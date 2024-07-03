import cv2
import numpy as np

img = cv2.imread('../mydata/qstar.jpeg')  # 这里需要灰度图片
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("original",img.copy())
img2 = img1.copy()
ret,th = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
_,contours,hierarchy = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[1]

# 轮廓近似值，有坑！！！
for contour in contours: # 注意有很多轮廓，需要遍历，如果只使用有一个可能没有值
    M = cv2.moments(contour)  # 1.轮廓的矩
    print(M)
    area = cv2.contourArea(contour)  # 2.轮廓面积
    print("contours area:", area)
    perimeter = cv2.arcLength(contour, True)  # 3.轮廓周长
    print('perimeter:', perimeter)
    appr = cv2.approxPolyDP(contour,5,True)
    cv2.drawContours(img,[appr],-1,[0,0,255],3) # 绘制轮廓一定要在彩色图片上面绘制，否则轮廓颜色不对
cv2.imshow("apprx",img)

cv2.waitKey(0)
cv2.destroyAllWindows()


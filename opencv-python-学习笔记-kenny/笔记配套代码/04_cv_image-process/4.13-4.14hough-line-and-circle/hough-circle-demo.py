import cv2
import numpy as np

img = cv2.imread('../mydata/opencv-logo-white.png')  # 填写图片名称
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray = cv2.boxFilter(gray,-1,(3,5)) # 两个值不一样的卷积核效果更好？
# gray = cv2.blur(gray,(3,3)) # 较差
# gray = cv2.medianBlur(gray,5) # 一般
gray = cv2.GaussianBlur(gray,(3,5),3) # 效果比较好
#参数需要慢慢调整，太大了不行，太小了也不行
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=30,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for circle in circles[0,:]:
    cv2.circle(img,(circle[0],circle[1]),circle[2],(0,255,0),2)
    cv2.circle(img,(circle[0],circle[1]),2,(0,255,0),3)


cv2.imshow("Circles", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

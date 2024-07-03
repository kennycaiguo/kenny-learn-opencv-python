import cv2

img = cv2.imread('gate.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 转化为灰度图
cv2.namedWindow('gray',cv2.WINDOW_NORMAL)
cv2.resizeWindow('gray',600,480)
cv2.imshow('gray',gray)
cv2.imwrite('graygate.jpg', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

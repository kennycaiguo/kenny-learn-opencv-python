import cv2
import numpy as np

#定义鼠标回调函数
def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)

cv2.namedWindow('mouse event',cv2.WINDOW_NORMAL)
cv2.resizeWindow('mouse event',640,360)

#设置鼠标回调
cv2.setMouseCallback('mouse event',mouse_callback,'123')

#用numpy生成黑图像
img = np.zeros((360,640,3),np.uint8)
while True:
    cv2.imshow('mouse event',img)
    key = cv2.waitKey(0)
    if key == ord('q'):
        break
cv2.destroyAllWindows()


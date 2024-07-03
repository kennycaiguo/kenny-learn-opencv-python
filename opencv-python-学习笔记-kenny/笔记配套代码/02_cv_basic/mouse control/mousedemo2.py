import numpy as np
import cv2

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),50,(0,255,0),-1)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('img',draw_circle)
while True:
    cv2.imshow('img',img)
    if cv2.waitKey(20) == 27: # 按esc退出
        break
cv2.destroyAllWindows()
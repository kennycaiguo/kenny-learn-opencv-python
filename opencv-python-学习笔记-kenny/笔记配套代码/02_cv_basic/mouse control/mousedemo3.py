"""
实现按下鼠标左键拖动绘制圆，按下鼠标右键拖动绘制矩形
"""
import cv2
import numpy as np

drawCircle = False
drawRect = False
ix,iy = -1,-1

def draw_shape(event,x,y,flags,param):
    global  drawCircle,drawRect,ix,iy
    if event == cv2.EVENT_LBUTTONDOWN:
        drawCircle = True
        drawRect = False
        ix,iy = x,y
    elif event == cv2.EVENT_RBUTTONDOWN:
        drawCircle = False
        drawRect = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        # if drawCircle:
        #     cv2.circle(img,(x,y),50,(0,255,255),-1)
        if drawRect:
            cv2.rectangle(img,(ix,iy),(x,y),(255,255,0),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (x, y), 50, (0, 255, 255), -1)
        drawCircle = False
    elif event == cv2.EVENT_RBUTTONUP:
        cv2.rectangle(img, (ix, iy), (x, y), (255, 255, 0), -1)
        drawRect = False


img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('img',draw_shape)
while True:
    cv2.imshow('img',img)
    if cv2.waitKey(20) == 27: # 按esc退出
        break
cv2.destroyAllWindows()
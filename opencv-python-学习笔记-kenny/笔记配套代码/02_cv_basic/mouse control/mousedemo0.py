"""
双击左键关闭窗口：
"""
import cv2

def mousecb(event,x,y,flags,param):
    global  open
    if event == cv2.EVENT_LBUTTONDBLCLK:
       open = False


cv2.namedWindow('mouse',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('mouse',mousecb)
img = cv2.imread('../jerry.png')
open = True
while open:
    cv2.imshow('mouse', img)
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()



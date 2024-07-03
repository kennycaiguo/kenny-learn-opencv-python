"""
opencv python实现点击鼠标左键视频翻转图片，点击右键垂直翻转图片
"""
import cv2

def flip(event,x,y,flags,param):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        img = cv2.flip(img,1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        img = cv2.flip(img,0)

img = cv2.imread('mygirl.jpg')
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('img',flip)
while True:
    cv2.imshow('img',img)
    if cv2.waitKey(20) == 27: # 按esc退出
        break
cv2.destroyAllWindows()
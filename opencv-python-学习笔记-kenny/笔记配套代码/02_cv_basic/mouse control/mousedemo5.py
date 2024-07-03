"""
opencv python 利用鼠标滚轮缩放图片,需要第三方库mouse,暂时不成功
"""
import cv2
import pynput as pyn


def on_scroll(x,y,dx,dy):
    global  img
    if dy > 0: # wheel up
        img = cv2.resize(img,(int(img.shape[1]*1.1),int(img.shape[0]*1.1)))
    if dy < 0:
        img = cv2.resize(img, (int(img.shape[1]*0.9), int(img.shape[0]*0.9)))

def scalepic(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEWHEEL:
        listener = pyn.mouse.Listener(on_scroll= on_scroll)
        listener.start()

img = cv2.imread('mygirl.jpg')

cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('img',scalepic)
cv2.resizeWindow('img',(600,480))
while True:
    cv2.imshow('img',img)
    if cv2.waitKey(20) == 27: # 按esc退出
        break
cv2.destroyAllWindows()


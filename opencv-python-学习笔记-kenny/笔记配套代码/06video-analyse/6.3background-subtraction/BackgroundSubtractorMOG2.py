import cv2
import numpy as np

cap = cv2.VideoCapture('../datas/vtest.avi')
fgbg = cv2.createBackgroundSubtractorMOG2() # 创建背景差分MOG对象
while True:
    ret,frame = cap.read()
    if not ret:
        break
    fgmask = fgbg.apply(frame)
    cv2.imshow("frame", fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

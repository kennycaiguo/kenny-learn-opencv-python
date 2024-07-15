import cv2
import numpy as np

cap = cv2.VideoCapture('../datas/vtest.avi')
# 获取卷积核
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG() # 创建背景差分MGM对象
while True:
    ret,frame = cap.read()
    if not ret:
        break
    fgmask = fgbg.apply(frame)
    # 需要使用形态学的开操作
    fgmask = cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,kernel)
    cv2.imshow("frame", fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

import cv2

# 创建视频窗口
cv2.namedWindow("video",cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',600,500)
cam = cv2.VideoCapture(0)

while True:
    ret,frame = cam.read()
    if not ret:
        break
    cv2.imshow('video',frame)
    key = cv2.waitKey(1) #这里不能为0，否则程序永远无法退出
    if key == 113:
        break

cam.release()
cv2.destroyAllWindows()



import cv2

#定义视频编码
four_cc = cv2.VideoWriter_fourcc(*'mp4v') # 注意：这里不支持divx

#创建VideoWriter实例
writer = cv2.VideoWriter("me.mp4",four_cc,30,(640,480))

#创建窗口
cv2.namedWindow('video cap',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video cap',640,480)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        break
    cv2.imshow('video cap',frame)
    writer.write(frame)
    key = cv2.waitKey(int(1000/30)) #这里的数值不能为0最好int(1000/上面的帧数)，如果数字太小，会发现视频播放很快
    if key == ord('q'):
        break
writer.release()
cap.release()
cv2.destroyAllWindows()


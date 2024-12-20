import cv2
import numpy as np

cap = cv2.VideoCapture('../datas/slow.mp4')
# feature params
feature_params = dict(
    maxCorners=100,
    qualityLevel=0.3,
    minDistance=7,
    blockSize=7
)
# Parameters for lucas kanade optical flow
Ik_params = dict(
    winSize=(15,15),
    maxLevel=2,
    criteria=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,10,0.03)
)
# Create some random colors
color = np.random.randint(0,255,(100,3))
ret,old_frame = cap.read() # 读取一帧
old_gray = cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY) # 转化为灰度图
# 使用Shi-tomas角点检测
p0 = cv2.goodFeaturesToTrack(old_gray,mask=None,**feature_params)
# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

#
while True:
    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # 计算光流
    p1,st,err = cv2.calcOpticalFlowPyrLK(old_gray,gray_frame,p0,None,**Ik_params)
    # Select good points
    good_new = p1[st==1]
    good_old = p0[st==1]
    # draw the tracks
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask,(a,b),(c,d), color[i].tolist(),2)
        frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
    img = cv2.add(frame,mask)
    cv2.imshow("result", img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
    old_gray = gray_frame.copy()
    # p0 = good_new.reshape(-1, 1, 2)
    p0 = p1
cv2.destroyAllWindows()
cap.release()

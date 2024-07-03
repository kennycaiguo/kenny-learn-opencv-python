import cv2
import numpy as np

img = cv2.imread('../mydata/sudoku.png')  # 填写图片名称
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray,30,150,apertureSize=3)
lines = cv2.HoughLinesP(edge,1,np.pi/180,100,minLineLength=100,maxLineGap=100)
for line in lines:
    x1,y1,x2,y2 = line[0]

    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)

cv2.imshow("Lines", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

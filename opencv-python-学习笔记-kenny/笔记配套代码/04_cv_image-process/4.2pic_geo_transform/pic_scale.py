import cv2
import numpy as np

img = cv2.imread('../mydata/messi2.png')  # 填写图片名称
#放大，方法1
# res = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
#放大，方法2
height, width = img.shape[:2]
res = cv2.resize(img,(width*2,height*2),interpolation=cv2.INTER_CUBIC)

#缩小
res_sm = cv2.resize(img,(width//2,height//2)) #注意这里dsize需要整数，所以需要使用整除符号
cv2.imshow("org",img)
cv2.imshow("result",res)
cv2.imshow('small',res_sm)

cv2.waitKey(0)
cv2.destroyAllWindows()

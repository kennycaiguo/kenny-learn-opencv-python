from utils import *
img = cv2.imread('jerry.png')
cv2.namedWindow("pic",cv2.WINDOW_NORMAL)
cv2.resizeWindow('pic',300,200)
# cv2.imshow("pic",img)
# key = cv2.waitKey(0)
# if key == 113: # 按下的是字母q
#     cv2.destroyAllWindows()

cv_show('pic',img)
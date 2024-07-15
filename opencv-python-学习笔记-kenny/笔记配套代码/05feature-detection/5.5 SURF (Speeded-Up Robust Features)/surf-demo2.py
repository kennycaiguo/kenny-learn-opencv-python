import cv2
import numpy as np

img = cv2.imread('../pic_datas/butterfly.jpg',0)
# 创建surf对象
surf = cv2.xfeatures2d_SURF.create(400)
# 关键点太多，无法在图片中显示。我们将它减少到大约50以将其绘制在图像上。
# 在匹配时，我们可能需要所有这些功能，但现在不需要。所以我们增加了Hessian阈值。
surf.setHessianThreshold(50000) #
# 现在我们尝试一下U-SURF，它不会检测关键点的方向。
surf.setUpright(True) #
kp = surf.detect(img,None)
img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
cv2.imshow("surf result", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

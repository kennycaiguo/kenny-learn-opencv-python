import cv2
import numpy as np

img = cv2.imread('../pic_datas/butterfly.jpg',0)
# 创建surf对象
surf = cv2.xfeatures2d_SURF.create(400)
# 关键点太多，无法在图片中显示。我们将它减少到大约50以将其绘制在图像上。
# 在匹配时，我们可能需要所有这些功能，但现在不需要。所以我们增加了Hessian阈值。
surf.setHessianThreshold(50000) #
# 现在我们尝试一下U-SURF，它不会检测关键点的方向。
# surf.setUpright(True) #
# So we make it to True to get 128-dim descriptors.我们检查描述符大小，如果它只有64-dim，则将其更改为128。
surf.setExtended(True)
kp,des = surf.detectAndCompute(img,None) # 如果只是使用detect方法是无法拿到描述符的
img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
print("descriptor",des.shape)
cv2.imshow("surf result", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

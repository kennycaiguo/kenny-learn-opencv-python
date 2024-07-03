import cv2
import numpy as np
from matplotlib import pyplot as plt
# 单模板匹配
target = cv2.imread('../mydata/lenas.png',0)  # 填写图片名称
template = cv2.imread('../mydata/template.jpeg',0)

# 获取template宽高
w, h = template.shape[::-1]
# Apply template Matching
res = cv2.matchTemplate(target,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(target,pt,(pt[0]+w,pt[1]+h),255,3)
cv2.imshow("result",target)
cv2.imwrite("match.png",target)
cv2.waitKey(0)
cv2.destroyAllWindows()

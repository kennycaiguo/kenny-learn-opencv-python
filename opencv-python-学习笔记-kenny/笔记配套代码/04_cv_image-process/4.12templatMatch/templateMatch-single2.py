import cv2
import numpy as np
from matplotlib import pyplot as plt
# 单模板匹配
img = cv2.imread('../mydata/lena.jpg',0)  # 填写图片名称
template = cv2.imread('../mydata/template.jpeg',0)
target2 = img.copy()
# 获取template宽高
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list ,注意:cv2.TM_CCORR效果不好
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for meth in methods:
    target = target2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(target,template,method)
    # cv2.normalize(res, res, 0, 1, cv2.NORM_MINMAX, -1)
    # 查找最大值和最小值
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
    # 不同的匹配方式有不同的处理方法
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0]+w,top_left[1]+h)
    cv2.rectangle(target,top_left,bottom_right,255,3)
    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(target, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

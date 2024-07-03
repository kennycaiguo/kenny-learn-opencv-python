# 凸包检测和凸缺陷
import cv2 as cv

# 读取图像
src1 = cv.imread("../mydata/hand2.jpg")
# 转换为灰度图像
gray = cv.cvtColor(src1, cv.COLOR_BGR2GRAY)
# 二值化
# ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
ret, binary = cv.threshold(gray, 70, 255, cv.THRESH_BINARY )
# 获取结构元素
k = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
# 开操作
binary = cv.morphologyEx(binary, cv.MORPH_OPEN, k)
# 轮廓发现
_,contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# 在原图上绘制轮廓，以方便和凸包对比，发现凸缺陷
cv.drawContours(src1, contours, -1, (0, 225, 0), 3)
for c in range(len(contours)):
    # 是否为凸包
    ret = cv.isContourConvex(contours[c])
    # 凸缺陷
    # 凸包检测，returnPoints为false的是返回与凸包点对应的轮廓上的点对应的index
    hull = cv.convexHull(contours[c], returnPoints=False)
    defects = cv.convexityDefects(contours[c], hull)
    print('defects', defects)
    for j in range(defects.shape[0]):
        s, e, f, d = defects[j, 0]
        start = tuple(contours[c][s][0])
        end = tuple(contours[c][e][0])
        far = tuple(contours[c][f][0])
        # 用红色连接凸缺陷的起始点和终止点
        cv.line(src1, start, end, (0, 0, 225), 2)
        # 用蓝色最远点画一个圆圈
        cv.circle(src1, far, 5, (225, 0, 0), -1)

# 显示
cv.imshow("result", src1)
cv.waitKey(0)
cv.destroyAllWindows()


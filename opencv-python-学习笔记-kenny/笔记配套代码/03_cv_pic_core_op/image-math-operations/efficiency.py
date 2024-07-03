import time
import cv2
"""
在图像处理中，由于每秒需要处理大量操作，因此处理图像的代码必须不仅要能给出正确的结果，同时还必须要快。所以在本小节中，
学习： - 衡量代码的性能。 - 一些优化代码性能的技巧 - 学习以下函数：cv.getTickCount, cv.getTickFrequency

除了OpenCV库之外，Python还提供了一个time模块，有助于测量执行时间。另一个profile模块可以获得有关代码的详细报告，
例如代码中每个函数所花费的时间，调用函数的次数等。如果你使用的是IPython，所有这些功能都以一个有好的方式整合到一起
使用 OpenCV 衡量程序效率
cv.getTickCount函数返回参考事件（如机器开启时刻）到调用此函数的时钟周期数。因此，如果在函数执行之前和之后都调用它，
则会获得用于执行函数的时钟周期数。

cv.getTickFrequency函数返回时钟周期的频率，或每秒钟的时钟周期数。所以，要想获得函数的执行时间，你可以执行以下操作：

e1 = cv.getTickCount()
# your code execution
e2 = cv.getTickCount()
time = (e2 - e1)/ cv.getTickFrequency()
也可以使用time模块的函数执行相同操作来替代cv.getTickCount，使用time.time()函数,然后取两次结果的时间差。
下面我们来测试图像运算的执行效率
"""
img1 = cv2.imread('messi2.png')  # 填写图片名称
img2 = cv2.imread('opencv-logo-white.png')  # 填写图片名称
# img2 = cv2.imread('./cv-white.png')  # 填写图片名称
cv2.imshow("white",img2)
# 设置快速时间
# start = cv2.getTickCount()
start = time.time()
# 获取logo图片的shape
rows,cols,chs = img2.shape
# 保存感兴趣区域
roi = img1[0:rows,0:cols]
gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) # 转化为灰度图
# 利用二值化获取蒙版
# ret,mask = cv2.threshold(gray,10,255,cv2.THRESH_BINARY) #这个案例中这两种是效果比较好的，有透明背景
ret,mask = cv2.threshold(gray,10,255,cv2.THRESH_BINARY_INV)#这个案例中这两种是效果比较好的，有透明背景
# 把蒙版翻转
mask_inv = cv2.bitwise_not(mask)

# 用翻转蒙版对感兴趣区域进行按位与操作
# img1_roi = cv2.bitwise_and(roi,roi,mask=mask_inv)
img1_roi = cv2.bitwise_and(roi,roi,mask=mask)
# 用蒙版对图片2进行按位与操作
# img2_and = cv2.bitwise_and(img2,img2,mask=mask)
img2_and = cv2.bitwise_and(img2,img2,mask=mask_inv)
# 将上面两个结果进行图像加法运算
dst = cv2.add(img1_roi,img2_and)
img1[0:rows,0:cols] = dst # 用结果覆盖感兴趣的区域
#显示结果
cv2.imshow("result", img1)
# 获取操作结束时间
# end = cv2.getTickCount()
end = time.time()
#计算
# time = (end-start)/cv2.getTickFrequency()
time = end-start
print("time:",time)
cv2.waitKey(0)
cv2.destroyAllWindows()


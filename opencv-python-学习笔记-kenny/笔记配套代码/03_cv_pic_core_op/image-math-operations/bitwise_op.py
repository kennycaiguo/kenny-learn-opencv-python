import cv2
"""
opencv python的图像位操作,将opencv的黑白logo图标经过处理后叠加到梅西图片里面
"""
img1 = cv2.imread('messi2.png')  # 填写图片名称
img2 = cv2.imread('opencv-logo-white.png')  # 填写图片名称
# img2 = cv2.imread('./cv-white.png')  # 填写图片名称
cv2.imshow("white",img2)
# 获取logo图片的shape
rows,cols,chs = img2.shape
# 保存感兴趣区域
roi = img1[0:rows,0:cols]
gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) # 转化为灰度图
# 利用二值化获取蒙版
# ret,mask = cv2.threshold(gray,10,255,cv2.THRESH_BINARY) #这个案例中这两种是效果比较好的，有透明背景
# ret,mask = cv2.threshold(gray,10,255,cv2.THRESH_MASK)
# ret,mask = cv2.threshold(gray,10,255,cv2.THRESH_OTSU)
# ret,mask = cv2.threshold(gray,10,255,cv2.THRESH_TOZERO)
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

cv2.waitKey(0)
cv2.destroyAllWindows()

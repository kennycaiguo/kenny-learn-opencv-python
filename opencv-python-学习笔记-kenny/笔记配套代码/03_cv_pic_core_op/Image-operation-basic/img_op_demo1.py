import cv2

img = cv2.imread('./messi.png')
#普通方法
# pic = img[:]
# px = pic[100,100] # 获取应该像素
# # print(px)
# blue = pic[100,100,0] #获取这个像素的蓝色通道的值
# print(blue)
# pic[100,100] = [255,0,255] # 修改那个像素的颜色:是BGR而不是RGB
# 使用numpy的ndarray的item方法,不太习惯
pic = img[:]
px0,px1,px2 = pic[100,100]
print(px0,px1,px2)
pic.itemset((100,100,0),px0*20)
pic.itemset((100,100,1),px1*0)
pic.itemset((100,100,2),px2*4)
# pic[50,50] = [px2,px1,px0]
print(pic[100, 100])
cv2.imshow('pic',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../mydata/home.jpg')  # 填写图片名称
color = ('b','g','r')
for i,col in enumerate(color):
    hist1 = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist1,color=col)
    plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

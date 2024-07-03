import  requests
import cv2
import numpy as np

img_url = "https://images.pexels.com/photos/1386604/pexels-photo-1386604.jpeg?auto=compress&cs=tinysrgb&w=600"
file = requests.get(img_url)
img = cv2.imdecode(np.fromstring(file.content,np.int8),1)
cv2.imshow('girl',img)
cv2.imwrite('mouse control/mygirl.jpg', img) # 保存图片
cv2.waitKey(0)
cv2.destroyAllWindows()
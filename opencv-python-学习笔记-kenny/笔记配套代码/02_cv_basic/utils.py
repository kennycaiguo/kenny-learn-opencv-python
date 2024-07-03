import  cv2

def cv_show(win,img):
    cv2.imshow(win,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

import cv2, numpy as np
path = "./Lab3/3-4.jpg"

def show():
    global key
    cv2.namedWindow("IMG3-4", flags = cv2.WINDOW_GUI_NORMAL)
    cv2.setWindowTitle('IMG3-4','Default') #gfedcb|abcdefgh|gfedcb
    cv2.imshow("IMG3-4",img_new)
    key = cv2.waitKey(0)
    cv2.setWindowTitle('IMG3-4','Constant')
    cv2.imshow("IMG3-4",img_new2)
    key = cv2.waitKey(0)
    cv2.setWindowTitle('IMG3-4','Isolated') 
    cv2.imshow("IMG3-4",img_new3)
    key = cv2.waitKey(0)
    cv2.setWindowTitle('IMG3-4','Reflect') #fedcba|abcdefgh|hgfedcb
    cv2.imshow("IMG3-4",img_new4)
    key = cv2.waitKey(0)
    cv2.setWindowTitle('IMG3-4','Reflect101') #like 1st
    cv2.imshow("IMG3-4",img_new5)
    key = cv2.waitKey(0)
    cv2.setWindowTitle('IMG3-4','Reflect_101') #as 1st
    cv2.imshow("IMG3-4",img_new6)
    key = cv2.waitKey(0)
    cv2.setWindowTitle('IMG3-4','Replicate') #aaaaaa|abcdefgh|hhhhhh
    cv2.imshow("IMG3-4",img_new7)
    key = cv2.waitKey(0)
    cv2.setWindowTitle('IMG3-4','Wrap') #what is it.... bcdefg|abcdefgh|abcdefg
    cv2.imshow("IMG3-4",img_new8)
    key = cv2.waitKey(0)

img = cv2.imread(path, flags = cv2.IMREAD_REDUCED_COLOR_8)

img_new = cv2.copyMakeBorder(img, top = 20, bottom = 20, left = 15, right = 15, borderType = cv2.BORDER_DEFAULT)
img_new2 = cv2.copyMakeBorder(img, top = 20, bottom = 20, left = 15, right = 15, borderType = cv2.BORDER_CONSTANT, value = (127,0,0))
img_new3 = cv2.copyMakeBorder(img, top = 20, bottom = 20, left = 15, right = 15, borderType = cv2.BORDER_ISOLATED)
img_new4 = cv2.copyMakeBorder(img, top = 20, bottom = 20, left = 15, right = 15, borderType = cv2.BORDER_REFLECT)
img_new5 = cv2.copyMakeBorder(img, top = 20, bottom = 20, left = 15, right = 15, borderType = cv2.BORDER_REFLECT101)
img_new6 = cv2.copyMakeBorder(img, top = 20, bottom = 20, left = 15, right = 15, borderType = cv2.BORDER_REFLECT_101)
img_new7 = cv2.copyMakeBorder(img, top = 20, bottom = 20, left = 15, right = 15, borderType = cv2.BORDER_REPLICATE)
img_new8 = cv2.copyMakeBorder(img, top = 20, bottom = 20, left = 15, right = 15, borderType = cv2.BORDER_WRAP)

show()
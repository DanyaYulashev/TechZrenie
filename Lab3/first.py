import cv2, numpy as np
path = "./Lab3/3-1.png"
path2 = "./Lab3/3-2.png"

def show(k):
    global key
    if k == 1:
        cv2.namedWindow("IMG3-1", flags = cv2.WINDOW_GUI_NORMAL)
        cv2.imshow("IMG3-1",img_blur1)
        key = cv2.waitKey(0)
        cv2.imshow("IMG3-1",img_box1)
        key = cv2.waitKey(0)
        cv2.imshow("IMG3-1",img_med1)
        key = cv2.waitKey(0)
        cv2.imshow("IMG3-1",img_gaus1)
        key = cv2.waitKey(0)
        cv2.imshow("IMG3-1",img_bi1)
        key = cv2.waitKey(0)
        cv2.imshow("IMG3-1",img_2d1)
        key = cv2.waitKey(0)
    if k == 2:
        cv2.namedWindow("IMG3-2", flags = cv2.WINDOW_GUI_NORMAL)
        cv2.imshow("IMG3-2",img_blur2)
        key = cv2.waitKey(0)
        cv2.imshow("IMG3-2",img_box2)
        key = cv2.waitKey(0)
        cv2.imshow("IMG3-2",img_med2)
        key = cv2.waitKey(0)
        cv2.imshow("IMG3-2",img_gaus2)
        key = cv2.waitKey(0)
        cv2.imshow("IMG3-2",img_bi2)
        key = cv2.waitKey(0)
        cv2.imshow("IMG3-2",img_2d2)
        key = cv2.waitKey(0)


img1 = cv2.imread(path, flags = cv2.IMREAD_COLOR)
img1Gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread(path2, flags = cv2.IMREAD_COLOR)
img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img_blur1 = cv2.blur(img1Gray, ksize = (7, 7), anchor=(-1, -1), borderType = cv2.BORDER_REPLICATE)
img_box1 = cv2.boxFilter(img1, ddepth = -1, ksize = (5, 5), anchor= (-1, -1), normalize = True, borderType = cv2.BORDER_CONSTANT)
img_med1 = cv2.medianBlur(img1, ksize =  21)
img_gaus1 = cv2.GaussianBlur(img1, ksize = (9, 9), sigmaX = 0, sigmaY = 0, borderType = cv2.BORDER_DEFAULT)
img_bi1 = cv2.bilateralFilter(img1, d = 9, sigmaColor = 9, sigmaSpace = 7, borderType = cv2.BORDER_REFLECT)
ker = np.full((3, 3),0.1)
img_2d1 = cv2.filter2D(img1Gray, ddepth = -1, kernel = ker, anchor = (-1, -1), borderType = cv2.BORDER_ISOLATED)

img_blur2 = cv2.blur(img2Gray, ksize = (7, 7), anchor=(-1, -1), borderType = cv2.BORDER_REPLICATE)
img_box2 = cv2.boxFilter(img2, ddepth = 24, ksize = (8, 8), anchor= (-1, -1), normalize = True, borderType = cv2.BORDER_CONSTANT)
img_med2 = cv2.medianBlur(img2, ksize =  13)
img_gaus2 = cv2.GaussianBlur(img2, ksize = (11, 11), sigmaX = 2, sigmaY = 0, borderType = cv2.BORDER_DEFAULT)
img_bi2 = cv2.bilateralFilter(img2Gray, d = 9, sigmaColor = 9, sigmaSpace = 7, borderType = cv2.BORDER_REFLECT)
ker2 = np.full((3, 4),0.1)
img_2d2 = cv2.filter2D(img2Gray, ddepth = -1, kernel = ker2, anchor = (-1, -1), borderType = cv2.BORDER_ISOLATED)

show(2)
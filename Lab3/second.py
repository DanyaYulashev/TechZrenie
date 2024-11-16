import cv2, numpy as np
path = "./Lab3/3-3.jpg"

img = cv2.imread(path, flags = cv2.IMREAD_COLOR)
# img1 =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_new = cv2.GaussianBlur(img, ksize = (17, 17), sigmaX = 2, sigmaY = 3, borderType = cv2.BORDER_DEFAULT)
# img_new = cv2.boxFilter(img, ddepth = -1, ksize = (5, 5), anchor= (-1, -1), normalize = True, borderType = cv2.BORDER_CONSTANT)

cv2.namedWindow("IMG",flags = cv2.WINDOW_AUTOSIZE)
cv2.imshow("IMG", img_new)
key = cv2.waitKey(0)
cv2.destroyAllWindows

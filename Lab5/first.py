import cv2
path = './Lab5/5-1.jpg'
path2 = './Lab5/5-2.jpg'
path3 = './Lab5/5-3.jpg'

img = cv2.imread(path, flags = cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(path2, flags = cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread(path3, flags = cv2.IMREAD_GRAYSCALE)

grad = cv2.Sobel(img, ddepth = cv2.CV_16U, dx = 1, dy = 1, ksize = 9, scale = 0.5, delta = 0, borderType = cv2.BORDER_DEFAULT)
grad2 = cv2.Sobel(img2, ddepth = cv2.CV_16U, dx = 1, dy = 1, ksize = 11, scale = 0.5, delta = 0, borderType = cv2.BORDER_DEFAULT)
grad3 = cv2.Sobel(img3, ddepth = cv2.CV_8U, dx = 2, dy = 0) + cv2.Sobel(img3, ddepth = cv2.CV_8U, dx = 0, dy = 2)

dst = cv2.Laplacian(img, ddepth = cv2.CV_8U, ksize = 5, scale = 0.2, delta = 0, borderType = cv2.BORDER_DEFAULT)
dst2 = cv2.Laplacian(img2, ddepth = cv2.CV_8U, ksize = 7, scale = 0.2, delta = 0, borderType = cv2.BORDER_DEFAULT)
dst3 = cv2.Laplacian(img3, ddepth = cv2.CV_8U, ksize = 5, scale = 0.2, delta = 0, borderType = cv2.BORDER_DEFAULT)

cv2.namedWindow("IMG", flags = cv2.WINDOW_NORMAL)
cv2.imshow("IMG", grad)
key = cv2.waitKey()
cv2.imshow("IMG", grad2)
key = cv2.waitKey()
cv2.imshow("IMG", grad3)
key = cv2.waitKey()
cv2.imshow("IMG", dst)
key = cv2.waitKey()
cv2.imshow("IMG", dst2)
key = cv2.waitKey()
cv2.imshow("IMG", dst3)
key = cv2.waitKey()
cv2.destroyAllWindows()
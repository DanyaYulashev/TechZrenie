import cv2

def cvt(img, code = cv2.COLOR_BGR2GRAY):
    imgG = cv2.cvtColor(img, code)
    return imgG

def medBlur(img, ksize = 25):
    imgMF = cv2.medianBlur(img, ksize)
    return imgMF

path1 = './Lab7/7_5_1.jpg'
path2 = './Lab7/7_5_2.jpg'
path3 = './Lab7/7_5_3.jpg'
path4 = './Lab7/7_5_4.jpg'
path5 = './Lab7/7_5_5.jpg'
path6 = './Lab7/7_5_6.jpg'

img = cv2.imread(path1, flags = cv2.IMREAD_COLOR)
img2 = cv2.imread(path2, flags = cv2.IMREAD_COLOR)
img3 = cv2.imread(path3, flags = cv2.IMREAD_COLOR)
img4 = cv2.imread(path4, flags = cv2.IMREAD_COLOR)
img5 = cv2.imread(path5, flags = cv2.IMREAD_COLOR)
img6 = cv2.imread(path6, flags = cv2.IMREAD_COLOR)

imgG = cvt(img)
img2G = cvt(img2)
img3G = cvt(img3)
img4G = cvt(img4)
img5G = cvt(img5)
img6G = cvt(img6)

imgMF1 = medBlur(imgG)
imgMF2 = medBlur(img2G)
imgMF3 = medBlur(img3G, 35)
imgMF4 = medBlur(img4G)
imgMF5 = medBlur(img5G)
imgMF6 = medBlur(img6G)

circles = cv2.HoughCircles(imgMF1, method = cv2.HOUGH_GRADIENT, dp = 2, minDist = 100, param1 = 275, param2 = 400, minRadius = 0, maxRadius = 1000)
circles2 = cv2.HoughCircles(imgMF2, method = cv2.HOUGH_GRADIENT, dp = 2, minDist = 100, param1 = 275, param2 = 400, minRadius = 0, maxRadius = 0)
circles3 = cv2.HoughCircles(imgMF3, method = cv2.HOUGH_GRADIENT, dp = 2, minDist = 500, param1 = 100, param2 = 500, minRadius = 0, maxRadius = 0)
circles4 = cv2.HoughCircles(imgMF4, method = cv2.HOUGH_GRADIENT, dp = 4, minDist = 500, param1 = 600, param2 = 400, minRadius = 0, maxRadius = 0)
circles5 = cv2.HoughCircles(imgMF5, method = cv2.HOUGH_GRADIENT, dp = 2, minDist = 100, param1 = 275, param2 = 400, minRadius = 0, maxRadius = 0)
circles6 = cv2.HoughCircles(imgMF6, method = cv2.HOUGH_GRADIENT, dp = 4, minDist = 10000, param1 = 475, param2 = 400, minRadius = 0, maxRadius = 0)

for i in range(0, circles.shape[1]):
    x = int(circles[0][i][0])
    y = int(circles[0][i][1])
    R = int(circles[0][i][2])
    cv2.circle(img, center = (x, y), radius = R, color = (0, 190, 255), thickness = 5, lineType = cv2.LINE_8)
for i in range(0, circles2.shape[1]):
    x = int(circles2[0][i][0])
    y = int(circles2[0][i][1])
    R = int(circles2[0][i][2])
    cv2.circle(img2, center = (x, y), radius = R, color = (0, 190, 255), thickness = 5, lineType = cv2.LINE_8)
for i in range(0, circles3.shape[1]):
    x = int(circles3[0][i][0])
    y = int(circles3[0][i][1])
    R = int(circles3[0][i][2])
    cv2.circle(img3, center = (x, y), radius = R, color = (0, 190, 255), thickness = 5, lineType = cv2.LINE_8)
for i in range(0, circles4.shape[1]):
    x = int(circles4[0][i][0])
    y = int(circles4[0][i][1])
    R = int(circles4[0][i][2])
    cv2.circle(img4, center = (x, y), radius = R, color = (0, 190, 255), thickness = 5, lineType = cv2.LINE_8)
for i in range(0, circles5.shape[1]):
    x = int(circles5[0][i][0])
    y = int(circles5[0][i][1])
    R = int(circles5[0][i][2])
    cv2.circle(img5, center = (x, y), radius = R, color = (190, 0, 255), thickness = 5, lineType = cv2.LINE_8)
for i in range(0, circles6.shape[1]):
    x = int(circles6[0][i][0])
    y = int(circles6[0][i][1])
    R = int(circles6[0][i][2])
    cv2.circle(img6, center = (x, y), radius = R, color = (190, 0, 255), thickness = 5, lineType = cv2.LINE_8)

cv2.namedWindow("IMG", flags = cv2.WINDOW_FREERATIO)
cv2.imshow("IMG", img)
key =cv2.waitKey()
cv2.namedWindow("IMG", flags = cv2.WINDOW_FREERATIO)
cv2.imshow("IMG", img2)
key =cv2.waitKey()
cv2.namedWindow("IMG", flags = cv2.WINDOW_FREERATIO)
cv2.imshow("IMG", img3)
key =cv2.waitKey()
cv2.namedWindow("IMG", flags = cv2.WINDOW_FREERATIO)
cv2.imshow("IMG", img4)
key =cv2.waitKey()
cv2.namedWindow("IMG", flags = cv2.WINDOW_FREERATIO)
cv2.imshow("IMG", img5)
key =cv2.waitKey()
cv2.namedWindow("IMG", flags = cv2.WINDOW_FREERATIO)
cv2.imshow("IMG", img6)
key =cv2.waitKey()
cv2.destroyAllWindows() 
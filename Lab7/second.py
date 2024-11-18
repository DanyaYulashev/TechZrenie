import cv2, numpy as np
from math import pi

def draw_line(x0, y0, x1, y1, img, color = (0, 139, 255), thickness = 3, lineType = cv2.LINE_8):
    cv2.line(img, (x0,y0), (x1,y1), color, thickness, lineType)

path = './Lab7/4-1.jpg'
img = cv2.imread(path, flags = cv2.IMREAD_COLOR)
ker = np.full((3, 3),0.1)

img_morph = cv2.morphologyEx(img, op = cv2.MORPH_OPEN, kernel = ker, anchor = (-1, -1), iterations = 2, borderType = cv2.BORDER_DEFAULT)

img2G = cv2.cvtColor(img_morph, cv2.COLOR_BGR2GRAY)
_, img2 = cv2.threshold(img2G, 75, 255, type = cv2.THRESH_BINARY_INV)

lines = cv2.HoughLinesP(img2, rho = 5, theta = pi/180, threshold = 1000, minLineLength = 50, maxLineGap = 5)
circles = cv2.HoughCircles(img2G, method = cv2.HOUGH_GRADIENT, dp = 2, minDist = 20, param1 = 80, param2 = 100, minRadius = 0, maxRadius = 0)
maxlen = 0
maxindexL = 0
maxarea = 0
maxindexC = 0
for i in range(0, lines.shape[0]):
    x0,y0,x1,y1 = lines[i][0][:]
    length = ((y1-y0)**2 + (x1-x0)**2)**(1/2)
    if maxlen <= length:
        maxlen = length
        maxindexL = i
for j in range(0, circles.shape[1]):
    x = int(circles[0][j][0])
    y = int(circles[0][j][1])
    R = int(circles[0][j][2])
    area = pi*(R**2)
    if maxarea <= area:
        maxarea = area
        maxindexC = j

x0, y0, x1, y1 = lines[maxindexL][0][:]
x = int(circles[0][maxindexC][0])
y = int(circles[0][maxindexC][1])
R = int(circles[0][maxindexC][2])

draw_line(x0, y0, x1, y1, img_morph)
cv2.circle(img_morph, center = (x, y), radius = R, color = (0, 139, 255), thickness = 3, lineType = cv2.LINE_8)

cv2.namedWindow("IMG", flags = cv2.WINDOW_AUTOSIZE)
cv2.imshow("IMG", img_morph)
key =cv2.waitKey()
cv2.destroyAllWindows()
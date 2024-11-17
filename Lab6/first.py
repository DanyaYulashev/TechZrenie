import cv2, numpy as np
from math import pi
path = './Lab6/6-1.png'


img = cv2.imread(path, flags = cv2.IMREAD_GRAYSCALE)

img2 = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

threshold, img = cv2.threshold(img, 127, 255, type = cv2.THRESH_BINARY)

ans = cv2.findContours(img, mode = cv2.RETR_TREE, method = cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = ans

# cv2.drawContours(img2, contours, contourIdx= -1, color = [255, 0, 255], thickness = 1, lineType = cv2.LINE_8)

for i in range(0,len(contours)):
    rect = cv2.boundingRect(contours[i])
    x, y, w, h = rect
    [x0, y0], r  = cv2.minEnclosingCircle(contours[i])
    per = cv2.arcLength(contours[i], closed = True)
    area = cv2.contourArea(contours[i])
    area2, triangle = cv2.minEnclosingTriangle(contours[i])
    x1,y1 = triangle[0][0][0], triangle[0][0][1]
    x2,y2 = triangle[1][0][0], triangle[1][0][1]
    x3,y3 = triangle[2][0][0], triangle[2][0][1]
    d1 = ((x2-x1)**2 + (y2-y1)**2)**0.5
    d2 = ((x3-x1)**2 + (y3-y1)**2)**0.5
    d3 = ((x2-x3)**2 + (y2-y3)**2)**0.5
    if ((0.95*per <= 2*pi*r <= 1.05*per) & (0.95*area <= pi*(r**2) <= 1.05*area)):
        cv2.drawContours(img2, contours, contourIdx = i, color = [255, 0, 0], thickness = 3, lineType = cv2.LINE_8)
    if ((0.95*per <= 2*w+2*h <= 1.05*per) & (0.95*area <= w*h <= 1.05*area)):
        cv2.drawContours(img2, contours, contourIdx = i, color = [0, 0, 255], thickness = 3, lineType = cv2.LINE_8)
    if (0.95*per <= d1+d2+d3 <= 1.05*per):
        cv2.drawContours(img2, contours, contourIdx = i, color = [255, 0, 139], thickness = 3, lineType = cv2.LINE_8)

    
print(d1,d2,d3)
cv2.namedWindow("IMG", flags = cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("IMG", img2)
key = cv2.waitKey()
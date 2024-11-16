import cv2, numpy as np
from math import pi, ceil
path = './Lab6/6-1.png'


img = cv2.imread(path, flags = cv2.IMREAD_GRAYSCALE)

img2 = cv2.cvtColor(img, cv2.IMREAD_COLOR)

ans = cv2.findContours(img, mode = cv2.RETR_TREE, method = cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = ans

# cv2.drawContours(img2, contours, contourIdx= -1, color = [255, 0, 0], thickness = 1, lineType = cv2.LINE_8)

for i in range(0,len(contours)):
    rect = cv2.boundingRect(contours[i])
    x, y, w, h = rect
    [x0, y0], r  = cv2.minEnclosingCircle(contours[i])
    len = cv2.arcLength(contours[i], closed = True)
    area = cv2.contourArea(contours[i])
    if (area == pi * (r**2)) or (len == 2*pi*r):
        cv2.drawContours(img2, contours, contourIdx = i, color = [255, 0, 0], thickness = 3, lineType = cv2.LINE_4)
    if (area == w * h) or (len == 2*h + 2*w):
        cv2.drawContours(img2, contours, contourIdx = i, color = [0, 0, 255], thickness = 3, lineType = cv2.LINE_4)

cv2.namedWindow("IMG", flags = cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("IMG", img2)
key = cv2.waitKey()